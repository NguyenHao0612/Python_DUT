#-----------------------------------------------------
# Turtle Graphics, Tuples and Importing Modules
#-----------------------------------------------------

import imp
from turtle import Screen,Turtle #from ---- import * : import everything
import turtle

tim = Turtle()

# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

for _ in range(4):
    tim.forward(100)
    tim.left(90)

# Importing Modules



screen = Screen()
screen.exitonclick()

# Draw a Dashed Line 
import turtle as t
import random
tim = t.Turtle()

# for _ in range (15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(num_sides):
    angle = 360 / num_sides 
    for _ in range(num_sides) :
        tim.forward(100)
        tim.right(angle)

for shape_side_n in  range(3,10) :
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

#---------------------------------------------------
import turtle as t
import random
tim = t.Turtle()
t.colormode(255)

def random_color() :
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

#----------------------------------------------------



