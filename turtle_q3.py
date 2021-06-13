# !/usr/bin/env python
# coding: utf-8
# Q3: Plot straight lines at different angles via turtle

import turtle as t 
import random

linelist = [ 'orange', 'purple', 'skyblue', 'aquamarine', 'deeppink', 'chocolate', 'yellow', 'salmon', 'royalblue', 'gold']

t.penup()
t.goto(0, 0)
t.left(90)

for i in range(20):
    color = random.choice(linelist) 
    t.pendown()
    t.pencolor(color)
    t.forward(150)
    t.penup()
    t.goto(0, 0)
    t.right(18)
t.done()