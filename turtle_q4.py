# !/usr/bin/env python
# coding: utf-8
# Q4: Plot polygon via turtle

import turtle as t

def user_require():
    n = int(input("你想畫幾邊形: "))
    while n < 3:
        print("至少為三角形!")
        n = int(input("你想畫幾邊形: "))

    length = int(input("多邊形的長度: ")) #默認為整數, 想要浮點數改成float()
    while length <= 0:
        print("邊長必須為正數!")
        length = int(input("多邊形的長度: "))

    color = input("多邊形的顏色: ") #此部分須注意，若不是turtle.pencolor()可接受的顏色字串，會出錯
    count = int(input("你想重複幾次: "))
    while count < 1:
        print("至少要畫一次!")
        count = int(input("你想重複幾次: "))
    return n, length, color, count


def poly(n, length, color):
    angle_turn = 180 - ((n-2)*180/n)
    t.pencolor(color)
    for i in range(n):
        t.forward(length)
        t.left(angle_turn)


def main():
    t.penup()
    t.goto(0,0)
    t.left(90)
    t.pendown()
    while True:
        n, length, color, count = user_require()
        for time in range(count):
            poly(n, length, color)
            t.left(20)
        next_draw = input("你還要繼續畫嗎(q為離開程式): ")
        if next_draw == 'q':
            break
    t.done() 


if __name__ == "__main__":
    main()