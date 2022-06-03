#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = int(input("значения x: "))
y = int(input("значения y: "))

max_1 = 0 # max^2(x^2y, xy^2)
min_2 = 0 # min^2(x-y, x+2y)
u = 0

expression_1 = ((x**2)*y) # x^2y
expression_2 = (x*(y**2)) # xy^2y
expression_3 = (x-y) # x-y
expression_4 = (x+2*y) # x+2y

if expression_1 > expression_2:
    max_1 = ((x**2)*y) ** 2
else:
    max_1 =(x*(y**2)) ** 2

if expression_3 < expression_4:
    min_2 = (x-y) ** 2
else:
    min_2 = (x+2*y) ** 2

u = max_1 + min_2

print(u)