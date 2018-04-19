from math import *
from turtle import *

# T
penup()
setposition(-200,0)
pendown()
lt(90)
fd(100)
lt(90)
fd(25)
bk(50)
penup()

# H
setposition(-160,0)
pendown()
rt(90)
fd(100)
bk(50)
rt(90)
fd(40)
lt(90)
fd(50)
bk(100)
penup()

# A
setposition(-100,0)
pendown()
rt(15)
fd(105)
rt(150)
fd(50)
rt(15+90)
fd(50*sin(15)-9)
bk(50*sin(15)-9)
rt(90-15)
bk(55)
penup()

# `
setposition(-120+50*sin(15),120)
pendown()
rt(120)
fd(40)
lt(105)
penup()

# N
setposition(-90+100*sin(15),0)
pendown()
fd(100)
rt(160)
fd(105)
lt(160)
fd(100)
penup()

# H
setposition(-90+100*sin(15)+60,0)
pendown()
fd(100)
bk(50)
rt(90)
fd(40)
lt(90)
fd(50)
bk(100)
penup()

n = input("")
# import math
# from turtle import *
#
# speed(0)
# penup()
# setposition(-200, 50)
# pendown()
# #N
# left(90)
# forward(100)
# right(180 - 45)
# forward(100 * math.sqrt(2))
# left(180 - 45)
# forward(100)
# penup()
# print(position())
#
# #G
# setposition (30,130)
# pendown()
# for i in range(3):
#     left(45)
#     forward(20*math.sqrt(2))
#     left(45)
#     forward(60)
# left(45)
# forward(20*math.sqrt(2))
# left(45)
# forward(20)
# penup()
# setposition(10,90)
# pendown()
# right(90)
# forward(40)
# penup()
#
# #O
# setposition(160, 130)
# pendown()
# left(90)
# for i in range(4):
#     left(45)
#     forward(20*math.sqrt(2))
#     left(45)
#     forward(60)
# penup()
#
# #C
# setposition(290, 130)
# pendown()
# for i in range(3):
#     left(45)
#     forward(20*math.sqrt(2))
#     left(45)
#     forward(60)
# left(45)
# forward(20*math.sqrt(2))
# penup()
# #.
# setposition(110, 30)
#
# n = input("")