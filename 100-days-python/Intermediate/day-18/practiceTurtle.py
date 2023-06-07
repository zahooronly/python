# from turtle import Turtle, Screen
from turtle import *
import random
timmy=Turtle()

timmy.shape("arrow")
# timmy.color("red")
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# for _ in range(1):
#     timmy.pencolor('green')
#     timmy.pendown()
#     timmy.forward(20)
    # timmy.penup()

# for _ in range(5):
#     timmy.color("green")
#     timmy.forward(50)
#     timmy.right(72)
# timmy.forward(50)
# for _ in range(4):
#     timmy.color("red")
#     timmy.forward(50)
#     timmy.right(90)
# timmy.forward(50)
# for _ in range(10):
#     timmy.color("blue")
#     timmy.forward(50)
#     timmy.right(36)
# timmy.forward(50)

colors=["dark blue","yellow","teal","dark cyan","aquamarine","magenta","red","green"]

# sides=int(input("Enter number of sides"))
sides=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20]
side=random.choice(sides)
angle=int(360/side)
for _ in range(side):
    timmy.color(random.choice(colors))
    timmy.forward(100)
    timmy.right(angle=angle)



screen= Screen()
screen.exitonclick()