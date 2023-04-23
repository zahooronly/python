# incomplete logic for rock paper scissor game

import random
listis = ['🪨 ', '📄', '✂️']
print(listis)
selectedItem = random.randint(0, 2)
inputItem = int(
    input("Enter your choice: 1 for rock, 2 for paper, 3 for scissor: \n"))
inputItem = inputItem-1
print(
    f"You chose {listis[inputItem]} and the computer chose {listis[selectedItem]}")
if inputItem == 2 and selectedItem == '📄':  # rock vs paper
    print("You win!")
elif inputItem == 2 and selectedItem == 1:  # scissor vs rock
    print("You lose!")
elif selectedItem > inputItem:
    print("You lose!")
elif selectedItem < inputItem:
    print("You win!")
else:
    print("It's a draw!")
