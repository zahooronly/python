# who will pay the bill
import random
# names = input("Enter the names of the people: ")
names = ['Zahoor Ahmad', 'Muhammad Faizan', 'Waqar Akram Bhutta']
# namelist = names.split(", ")
selectedPerson = random.choice(names)
print(f"{selectedPerson} will pay the bill today.")
