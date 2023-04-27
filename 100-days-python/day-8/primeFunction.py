number=int(input('Enter a number to check: '))
def primeNumberChecker(number):
    numberisPrime=True
    for i in range(2,number):
        if number%i==0:
            numberisPrime=False
    if numberisPrime:
        print(f'{number} is a Prime Number')
    else:
        print(f'{number} is a Not Prime Number')
primeNumberChecker(number)