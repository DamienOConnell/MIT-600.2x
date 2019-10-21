#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-


class Food(n, c, w):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
        return self

    def get_name():
        return self.name

    def get_value():
        return self.value / self.calories


foods = []

with open("foods", "r", encoding="utf-8") as ff:
    food_data = ff.readlines()
n = ""
v = 0
w = 0

for line in food_data:
    print(line)
    n, v, w = ",".split(line)
    foods.append(Food(n, v, w))

breakpoint()
