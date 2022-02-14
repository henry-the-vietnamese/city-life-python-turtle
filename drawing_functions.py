#!/usr/bin/python3

#
# File:         drawing_functions.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         22-Jul-21
# Description:  A list of user-defined functions that assist in drawing
#               repetitive shapes.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#


# ------------------------------- Module Import -------------------------------
import turtle


# ---------------------------- Function Definitions ---------------------------
def set_turtle(animal, pencolour, fillcolour, pensize):
    animal.shape('turtle')
    animal.color(pencolour, fillcolour)
    animal.pensize(pensize)
    animal.speed(0)


def move_turtle(animal, x, y):
    animal.pu()
    animal.goto(x, y)
    animal.pd()


def draw_window(window, x, y):
    move_turtle(window, x, y)
    window.begin_fill()
    window.lt(90)
    window.fd(50)
    for _ in range(4):
        window.lt(-90)
        window.fd(50)
    window.end_fill()
    window.lt(-90)
    window.fd(25)
    window.lt(-90)
    window.fd(50)
    window.fd(-25)
    window.lt(90)
    window.fd(25)
    window.fd(-50)


def draw_wheel(wheel, x1, y1):
    move_turtle(wheel, x1, y1)
    wheel.begin_fill()
    wheel.circle(15)
    wheel.end_fill()
    a = 0
    if x1 == -200:
        x2, y2 = -200, -325
    elif x1 == -105:
        x2, y2 = -94, -327
    while a < 360:
        move_turtle(wheel, x2, y2)
        wheel.setheading(0)
        wheel.lt(a)
        wheel.fd(15)
        a += 45


def draw_star(star, x, y):
    move_turtle(star, 230, 63)
    star.begin_fill()
    for i in range(5):
        star.fd(50)
        star.lt(-144)
    star.end_fill()
    star.hideturtle()


def draw_eye(eye, x, y):
    move_turtle(eye, x, y)
    eye.lt(90)
    eye.circle(4)


def draw_leg(leg, x, y):
    move_turtle(leg, x, y)
    leg.seth(270)
    leg.begin_fill()
    leg.fd(10)
    leg.lt(-90)
    leg.circle(5)
    leg.end_fill()
