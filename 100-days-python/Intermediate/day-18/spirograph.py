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

# tom.pensize(10)
def spiroGraph(gap):
    for _ in range(int(360/gap)):
        tom.speed("fastest")
        tom.circle(100)
        tom.color(randomColor())
        tom.setheading(tom.heading()+gap)

spiroGraph(10)
screen= tl.Screen()
screen.exitonclick()