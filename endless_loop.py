# !/usr/bin/env python
# coding: utf-8
# while loop example 

print("輸入一個非負整數: ", end = "")
number = int(input())
while (number >= 0):
    print("請再輸入一次:", end = "")
    number = int(input())
print("程序結束")