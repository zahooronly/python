print(''''          Welcome to Treasure Island.
        Your mission is to find the treasure.''')
# Write your code below this line 👇
direction = input(
    'You\'re at a cross road. Where do you want to go? Type "left" or "right": ')
if direction == 'right' or direction == 'Right' or direction == 'RIGHT':
    print('You fell into a hole. Game Over.')
elif direction == 'left' or direction == 'Left' or direction == 'LEFT':
    print('Congrats, you\'re still alive!')
    newDirection = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across: ')
    if newDirection == 'swim' or newDirection == 'Swim' or newDirection == 'SWIM':
        print('You were attacked by an angry trout. Game Over.')
    elif newDirection == 'wait' or newDirection == 'Wait' or newDirection == 'WAIT':
        door = input(
            'You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? ')
        if door == 'Red' or door == 'red' or door == 'RED' or door == 'Blue' or door == 'blue' or door == 'BLUE':
            print('It\'s a room full of fire. Game Over.')
        elif door == 'Yellow' or door == 'yellow' or door == 'YELLOW':
            print('You found the treasure! You Win!')
