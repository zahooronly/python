# roller coaster ride for the mid life crisis
height = float(input('What is your height in centimeters? '))
if height >= 120:
    print('You can ride the roller coaster!')
    age = int(input('What is your age? '))
    if age < 12:
        print('Please pay $5.')
    elif age <= 18:
        print('Please pay $7.')
    elif age >= 45 and age <= 55:
        print('Everything will be okay. Please pay $0.')
    else:
        print('Please pay $12.')
else:
    print('Sorry, you have to grow taller before you can ride.')
