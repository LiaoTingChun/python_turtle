# !/usr/bin/env python
# coding: utf-8
# Q1: At random coordinates, plot circles with random radius via turtle

import turtle
import random

for i in range(10):
    x_center , y_center = random.uniform(-300,300), random.uniform(-300,300)
    radius = random.uniform(5,250)
    turtle.up()
    turtle.setpos(x_center,  y_center)
    turtle.down()
    turtle.circle(radius)
    turtle.up()
    turtle.home()