# write all letters including uppercase and lowercase
import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','_','+']
print("Welcome to the MyPassword Generator!\n")
nLetters=int(input("How many letters would you like in your password?\n"))
nNumbers=int(input("How many numbers would you like in your password?\n"))
nSymbols=int(input("How many symbols would you like in your password?\n"))
# Easy Password
passwordList=""
for char in range(1,nLetters+1):
    passwordList+=random.choice(letters)
for char in range(1,nNumbers+1):
    passwordList+=random.choice(numbers)
for char in range(1,nSymbols+1):
    passwordList+=random.choice(symbols)
print("Your Simple Password is: "+passwordList)
passwordListHard=[]
for char in range(1,nLetters+1):
    passwordListHard.append(random.choice(letters))
for char in range(1,nNumbers+1):
    passwordListHard.append(random.choice(numbers))
for char in range(1,nSymbols+1):
    passwordListHard.append(random.choice(symbols))
random.shuffle(passwordListHard)
# print(passwordListHard)
password=''
for char in passwordListHard:
    password+=char
print("Your Hard Password is: "+password)