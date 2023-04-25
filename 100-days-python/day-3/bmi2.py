# create a bmi calculator
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = round((weight/(height**2)), 2)
if bmi < 18.5:
    print("Your BMI is: ", bmi, "You are underweight.")
elif bmi < 25:
    print("Your BMI is: ", bmi, "You have a normal weight.")
elif bmi < 30:
    print("Your BMI is: ", bmi, "You are slightly overweight.")
elif bmi < 35:
    print("Your BMI is: ", bmi, "You are obese.")
else:
    print("Your BMI is: ", bmi, "You are clinically obese.")


# print("Your BMI is: ", bmi)
