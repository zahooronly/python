# from turtle import Turtle, Screen
from turtle import *
import random
tom=Turtle()

tom.shape("arrow")
colors=["dark blue","yellow","teal","dark cyan","aquamarine","magenta","red","green"]
color=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","wheat","SlateGray","SeaGreen"]
directions=[0,90,180,270]
tom.pensize(15)
for _ in range(50):
    tom.color(random.choice(color))
    tom.forward(50)
    tom.setheading(random.choice(directions))



screen= Screen()
screen.exitonclick()