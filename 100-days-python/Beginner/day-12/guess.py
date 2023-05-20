import logo as logo
import random as rnd
print(logo.logo)
randomNumber=rnd.randrange(1,100,1)
def guessTheNumber():
    """_summary_
    This Function is a Guess the number game.
    This function auto generates a number between 1-100,
    takes input from user and then checks if user has guess right or not.
    """
    def notGuessedRight(n):
        """_summary_
            If user has guess wrong. So what else he can do? This function is to help the user to guess right
        Args:
            n (int): takes an argument so that it can provide input to the loop.
        """
        if (n-(i+1))>=0:
            if userInput<randomNumber:
                print(f"Guessed wrong! You have {n-(i+1)} chances remaining...")
                print('Your Guess is too small!')
            elif userInput>randomNumber:
                print(f"Guessed wrong! You have {n-(i+1)} chances remaining...")
                print('Your Guess is too High!')
        elif (n-(i+1)<0):
            print('You lose!\nYou have no more chances to guess :(')
    gameLevel=input("Want to play 'Easy' or 'Hard' level Game? ").lower()
    if gameLevel=='easy':
        print('You have 10 chances to Guess.')
        for i in range(10):
            userInput=int(input('Enter a number: '))
            if userInput==randomNumber:
                print(f'You Win!\nYou Guessed the right Number which is {randomNumber}')
                break
            else:
                notGuessedRight(10)
    elif gameLevel=='hard':
        print('You have 5 chances to Guess.')
        for i in range(4):
            userInput=int(input('Enter a number: '))
            if userInput==randomNumber:
                print(f'You Win!\nYou Guessed the right Number which is {randomNumber}')
                break
            else:
                notGuessedRight(5)
    else:
        print('Please Enter a valid argument!')
        guessTheNumber()
guessTheNumber()

