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


tom.shape("arrow")
colors=["dark blue","yellow","teal","dark cyan","aquamarine","magenta","red","green"]
color=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","wheat","SlateGray","SeaGreen"]
directions=[0,90,180,270]
tom.pensize(15)
for _ in range(50):
    tom.color(randomColor())
    tom.forward(50)
    tom.setheading(random.choice(directions))



screen= tl.Screen()
screen.exitonclick()