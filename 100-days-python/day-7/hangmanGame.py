import random
import hangmanArt as stages
import wordList as letterss
# print(stages)
print(stages.hangmanLogo)
numberOfLives=len(stages.stages)-1
# letters=['Ali','Abbas','Ammar','Ahsan','Qamar','Qasim','Qadeer','Bilal','Babar','Bilaw']
letters=letterss.names
chosenWord=random.choice(letters).lower()

# print(chosenWord)
chosenWordList=[]
for _ in range(len(chosenWord)):
    chosenWordList.append('_')
print(chosenWordList)


endOfTheGame=False
while not endOfTheGame:
    letter=input('Enter a letter: ').lower()
    for position in range(len(chosenWord)):
        i=chosenWord[position]
        if i==letter:
            chosenWordList[position]=letter
    if letter not in chosenWord:
        print('Not Matched :(')
        numberOfLives-=1
        if numberOfLives==0:
            endOfTheGame=True
            print(stages.you_lose)
    print(chosenWordList)
    if '_' not in chosenWordList:
        endOfTheGame=True
        print(stages.you_win)
        # print('You Win!')
# print(chosenWordList)

# chosenWordList.find(letter)