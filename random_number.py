# !/usr/bin/env python
# coding: utf-8
# random example 

import random

def roll_dice():
    roll_list = []
    for i in range(6):
        number = random.randint(1,6)
        roll_list.append(number)
    roll_set = set(roll_list)
    if len(roll_set) == 6:
        return roll_dice()
    else:
        idx = 0
        for times in range(3):
            print("第一個數字:", roll_list[idx+times], "第二個數字:", roll_list[idx+times+1], "\n")
            idx += 1
            
roll_dice()