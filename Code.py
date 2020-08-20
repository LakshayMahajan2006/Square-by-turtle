# Square-by-turtle

#import packages
import turtle
import math
import random

#Setting up a screen
wn = turtle.Screen()
wn.title("By Lakshay Mahajan")

# Square
#Start printing square
lakshay = turtle.Turtle()

lakshay.color("black", "cyan")

lakshay.begin_fill()
lakshay.forward(100)
lakshay.left(90)
lakshay.forward(100)
lakshay.left(90)
lakshay.forward(100)
lakshay.left(90)
lakshay.forward(100)
lakshay.end_fill()

lakshay.penup()
lakshay.forward(150)
lakshay.pendown()

lakshay.begin_fill()
lakshay.forward(100)
lakshay.left(90)
lakshay.forward(100)
lakshay.left(90)
lakshay.forward(100)
lakshay.left(90)
lakshay.forward(100)
lakshay.end_fill()


turtle.done()
