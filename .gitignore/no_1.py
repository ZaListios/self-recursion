#self recursion
from turtle import *
colormode(255)
c = 0
pencolor(225,0,0)
bgcolor(255,0,0)
title("self recursion")
screensize(canvwidth=1500, canvheight=1500)
pencolor(255,0,0)
hideturtle()
penup()
goto(-400,250)
pendown()
speed(0)
a = 800
while 1:
  for i in range(4):
    fd(a)
    rt(90)
  a /= 1.1
  penup()
  setx(xcor()+a/8)
  sety(ycor()+4)
  c += 5
  if c >= 256:
    break
  pencolor(255,c,0)
  pendown()
  if a <= 0.01:
    break

