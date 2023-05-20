import extraImport as file
print(file.cCipherText)
userChoice=input('What do you want? "Encode" or "Decode" ').lower()
text=input('Enter your text: ').lower()
shiftNumber=int(input('Enter the shift number: '))
# userText=[]
# for i in text:
#     userText.append(i)
# print(userText)
def encrypt(text,shiftNumber):
    encryptedText=''
    for i in text:
        indexI=file.alphabets.index(i)
        newIndex=indexI+shiftNumber
        # newLetter=file.alphabets[newIndex]
        encryptedText+=file.alphabets[newIndex]
    print(f'Your Encrypted Text is "{encryptedText}"')
def decrypt(text,shiftNumber):
    encryptedText=''
    for i in text:
        indexI=file.alphabets.index(i)
        newIndex=indexI-shiftNumber
        # newLetter=file.alphabets[newIndex]
        encryptedText+=file.alphabets[newIndex]
    print(f'Your Encrypted Text is "{encryptedText}"')
    
if userChoice=='encode':
    encrypt(text,shiftNumber)
elif userChoice=='decode':
    decrypt(text,shiftNumber)