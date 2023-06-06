import cv2
import numpy as np
import tensorflow as tf

model_path = "path_to_model/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8"
model = tf.saved_model.load(model_path)

def detect_weapons(image):
    # Preprocess the image
    input_tensor = tf.convert_to_tensor(image)
    input_tensor = input_tensor[tf.newaxis, ...]

    # Run inference
    model_fn = model.signatures['serving_default']
    output_dict = model_fn(input_tensor)

    num_detections = int(output_dict['num_detections'])
    classes = output_dict['detection_classes'][0].numpy().astype(np.uint8)
    scores = output_dict['detection_scores'][0].numpy()
    boxes = output_dict['detection_boxes'][0].numpy()

    # Draw bounding boxes around detected weapons
    for i in range(num_detections):
        if scores[i] > 0.5:  # Set a threshold for confidence
            class_id = classes[i]
            ymin, xmin, ymax, xmax = boxes[i]

            # Convert normalized coordinates to pixel values
            im_height, im_width, _ = image.shape
            ymin = int(ymin * im_height)
            xmin = int(xmin * im_width)
            ymax = int(ymax * im_height)
            xmax = int(xmax * im_width)

            # Draw bounding box
            cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

    return image


image_path = "path_to_image/image.jpg"
image = cv2.imread(image_path)

output_image = detect_weapons(image)

# Display the output image
cv2.imshow("Weapon Detection", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
