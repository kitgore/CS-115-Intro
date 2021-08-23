# Written by Dominick DiMaggio for Prof. Antonio Nicolosi's CS 115 at Stevens Institute of Technology, 2020

from turtle import Turtle, Screen
import time

def check_num(num):
    print()
    print("Task 1: Correct!" if num == 1 else "Task 1: " + str(num) + " does not equal 1")

def check_magnitude(num):
    print()
    if num > 201.479 and num < 201.481:
        print("Task 2: Correct!")
    else:
        print("Task 2: " + str(num) + " is not the correct magnitude")

def draw_shape(coords):
    turtle = Turtle()
    turtle.speed(1)
    turtle.pensize(10)
    turtle.hideturtle()
    turtle.color('black')

    if(len(coords) > 0):
        turtle.speed(0)
        turtle.penup()
        turtle.setposition(coords[0])
        turtle.pendown()
        turtle.speed(1)
    else:
        return   

    for c in coords[1:]:
        turtle.goto(c)

    time.sleep(1)
    turtle.clear()