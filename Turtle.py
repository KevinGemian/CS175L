#Kevin Gemian
#CS 107-01
#Turtle
import math
import turtle
window_width = 400
window_height = 400
animation_speed = 0
num_sides = 8
length = 100
angle = 45
text_x = -5
text_y = -10
turtle.setup (window_width, window_height)
s = length
x = s / math.sqrt(2)
diameter = s + (2 * x)
turtle.penup()
turtle.goto(-50,(diameter/2))
turtle.pendown()
turtle.color("red")
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(8):
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()
#white octogon
num_sides = 8
length = 90
angle = 45
text_x = -5
text_y = -10
s = length
x = s / math.sqrt(2)
diameter = s + (2 * x)
turtle.color("white")
turtle.pensize(10)
turtle.penup()
turtle.goto(-45,(diameter/2))
turtle.pendown()
for i in range(8):
    turtle.forward(length)
    turtle.right(angle)
turtle.penup()
turtle.goto(-85,-36)
turtle.pendown()
turtle.write('STOP', font=("Veranda",
                        50, 'normal'))
turtle.done()