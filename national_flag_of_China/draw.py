from turtle import *
import math

flagwidth = 1200
setup(width=flagwidth, height=2/3*flagwidth, startx=None, starty=None)
bgcolor("red")

def draw_star(point,radius,angle=0):
    x,y = point
    penup()
    setx(x)
    sety(y)
    left(180-18+angle)
    forward(radius)
    right(180-18)
    pendown()
    color('yellow', 'yellow')
    begin_fill()
    for i in range(0,5):
        a = radius * math.cos(54/180*math.pi) / math.cos(36/180*math.pi)
        forward(a)
        left(72)
        forward(a)
        right(144)
    end_fill()

cell = flagwidth / 2 / 15
rbig = cell * 3
rsmall = cell * 1

draw_star((-10*cell,5*cell),rbig)
draw_star((-5*cell,8*cell),rsmall,-math.tanh(3/5)*180)
draw_star((-3*cell,6*cell),rsmall,-math.tanh(1/7)*180)
draw_star((-3*cell,3*cell),rsmall,math.tanh(2/7)*180)
draw_star((-5*cell,cell),rsmall,math.tanh(4/5)*180)

done()
