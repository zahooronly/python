# smallPizza = 15
# mediumPizza = 20
# largePizza = 25
pizzaSize = input("What size pizza do you want? S, M, or L: ")
addPepperoni = input("Do you want pepperoni? Y or N: ")
extraCheese = input("Do you want extra cheese? Y or N: ")
if pizzaSize == 'S':
    bill = 15
    if addPepperoni == 'Y':
        bill += 2
    if extraCheese == 'Y':
        bill += 1
elif pizzaSize == 'M':
    bill = 20
    if addPepperoni == 'Y':
        bill += 3
    if extraCheese == 'Y':
        bill += 1
elif pizzaSize == 'L':
    bill = 25
    if addPepperoni == 'Y':
        bill += 3
    if extraCheese == 'Y':
        bill += 1
print(f'Your final bill is: ${bill}.')
