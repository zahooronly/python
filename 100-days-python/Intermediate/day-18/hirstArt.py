# from turtle import Turtle, Screen
import turtle as tl
import random
tom=tl.Turtle()
tl.colormode(255)
def randomColor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
tom.speed("fastest")
tom.penup()
tom.color("white")
tom.setheading(225)
tom.forward(300)
tom.setheading(0)
dots=100
for dott in range(1,dots+1):
    tom.dot(20,randomColor())
    tom.forward(50)
    if dott%10==0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)
screen= tl.Screen()
screen.exitonclick()