# !/usr/bin/env python
# coding: utf-8
# Q2: Plot stars with user requirements via turtle

import turtle as t 
import random


# 2-(1) 用戶輸入7種顏色 
color_check = ['red', 'orange', 'yellow', 'green', 'blue', 'skyblue', 'purple']
color_list = []
for i in range(7):
    color = input("輸入7種顏色: ")
    while color not in color_check:
        print("請輸入正確顏色!")
        color = input("輸入7種顏色: ")
    color_list.append(color)


# 2-(2) 隨機生成10個(x, y)座標
'''
coordinate = []
for i in range(10):
    x, y = random.randint(-300, 300), random.randint(-300, 300)
    coordinate.append(tuple([x, y]))
'''


# 2-(3) 隨機設定10個線條長度
'''
line_length = []
for i in range(10):
    length = random.randint(30, 200)
    line_length.append(length)
'''


# 2-(5) draw_star fuction
def draw_star(length, color):
    t.pendown()
    t.pencolor('black')
    t.fillcolor(color) 
    t.begin_fill()  
    for i in range(5): 
        t.forward(length)
        t.right(144) 
    t.end_fill()


# 2-(6)繪製10個五角星
for i in range(10):
    x, y = random.randint(-300, 300), random.randint(-300, 300) #生成隨機座標
    length = random.randint(30, 200) #生成隨機線條長度
    color = random.choice(color_list) #隨機選擇一種顏色
    t.penup()
    t.goto(x, y)
    draw_star(length, color)
t.done()