import turtle

# Setting the window
win = turtle.Screen()

width = 1250
height = 650

win.setup(width, height)

# Creating the first pen
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.pensize(2)
pen1.penup()

border_x, border_y = 135, 25

# K
pen1.goto(-width/2 + border_x, height/2 - border_y)
pen1.pendown()
pen1.setheading(270)
pen1.forward(100)
pen1.goto(pen1.xcor(), pen1.ycor()+40)
pen1.goto(pen1.xcor() + 50, pen1.ycor() + 60)
pen1.penup()
pen1.goto(pen1.xcor() - 45, pen1.ycor() - 55)
pen1.pendown()
pen1.goto(pen1.xcor() + 45, pen1.ycor() - 45)
pen1.setheading(0)
pen1.penup()

# Fullstop
pen1.forward(40)
pen1.pendown()
for i in range(4):
    pen1.left(90)
    pen1.forward(20)
pen1.penup()

# V
pen1.forward(15)
pen1.sety(pen1.ycor()+100)
pen1.pendown()
pen1.goto(pen1.xcor() + 35, pen1.ycor()-100)
pen1.goto(pen1.xcor() + 35, pen1.ycor()+100)
pen1.penup()

# O
pen1.goto(pen1.xcor()+45, pen1.ycor()-100)
pen1.pendown()
pen1.setheading(90)
pen1.forward(100)
pen1.right(90)
pen1.forward(50)
pen1.right(90)
pen1.forward(100)
pen1.right(90)
pen1.forward(50)
pen1.penup()

# Fullstop
pen1.backward(85)
pen1.pendown()

for i in range(3):
    pen1.forward(20)
    pen1.right(90)
pen1.forward(20)
pen1.penup()

# N
pen1.goto(pen1.xcor()+15, pen1.ycor())
pen1.pendown()
pen1.backward(100)
pen1.goto(pen1.xcor()+50, pen1.ycor()-100)
pen1.setheading(90)
pen1.forward(100)
pen1.penup()

# Fullstop
pen1.goto(pen1.xcor()+15, pen1.ycor()-100)
pen1.pendown()
for i in range(4):
    pen1.forward(20)
    pen1.right(90)
pen1.penup()

# G
pen1.goto(pen1.xcor()+15 + 20, pen1.ycor())
pen1.pendown()
pen1.forward(100)
pen1.right(90)
pen1.forward(45)
pen1.backward(45)
pen1.right(90)
pen1.forward(100)
pen1.left(90)
pen1.forward(35)
pen1.left(90)
pen1.forward(40)
pen1.right(90)
pen1.forward(20)
pen1.right(90)
pen1.forward(40)
pen1.penup()

# Fullstop
pen1.left(90)
pen1.forward(15+20)
pen1.pendown()
for i in range(4):
    pen1.left(90)
    pen1.forward(20)
pen1.penup()

# C
pen1.forward(15)
pen1.pendown()
pen1.goto(pen1.xcor(), pen1.ycor()+100)
pen1.forward(50)
pen1.backward(50)
pen1.right(90)
pen1.forward(100)
pen1.left(90)
pen1.forward(50)
pen1.penup()

# P
pen1.forward(50)
pen1.pendown()
pen1.left(90)
pen1.forward(100)
pen1.right(90)
pen1.forward(45)
pen1.right(90)
pen1.forward(45)
pen1.right(90)
pen1.forward(45)
pen1.penup()

# a
pen1.goto(pen1.xcor()+45+15, pen1.ycor() - (100-45))
pen1.pendown()
pen1.right(90)
pen1.forward(25)
pen1.right(90)
pen1.forward(35)
pen1.right(90)
pen1.forward(25)
pen1.right(90)
pen1.forward(35)
pen1.backward(35)
pen1.sety(pen1.ycor() + 35+15)
pen1.forward(35)
pen1.penup()

# n
pen1.goto(pen1.xcor()+35+15, pen1.ycor()-35-15)
pen1.pendown()
pen1.right(90)
pen1.forward(50)
pen1.right(90)
pen1.forward(40)
pen1.sety(pen1.ycor()-50)
pen1.penup()

# v
pen1.goto(pen1.xcor()+15, pen1.ycor() + 50)
pen1.pendown()
pen1.goto(pen1.xcor()+25, pen1.ycor() - 50)
pen1.goto(pen1.xcor()+25, pen1.ycor() + 50)
pen1.penup()

# e
pen1.forward(15)
pen1.pendown()
pen1.forward(40)
pen1.right(90)
pen1.forward(20)
pen1.right(90)
pen1.forward(40)
pen1.goto(pen1.xcor(), pen1.ycor()+20)
pen1.goto(pen1.xcor(), pen1.ycor()-50)
pen1.right(90)
pen1.goto(pen1.xcor()+40, pen1.ycor())
pen1.penup()

# l
pen1.right(90)
pen1.forward(45)
pen1.pendown()
pen1.backward(30)
pen1.sety(pen1.ycor()+100)
pen1.penup()

# line 1
pen1.goto(pen1.xcor()+35, pen1.ycor()-120)
temp0 = pen1.xcor()
pen1.pendown()
pen1.pensize(3)
pen1.setx(-width/2 + border_x)
pen1.penup()

# line 2
pen1.goto(pen1.xcor() - 25, pen1.ycor() - 20)
pen1.pendown()
pen1.pensize(4)
pen1.setx(temp0 + 25)
pen1.pensize()
pen1.hideturtle()

# To start pen 2 with reference to pen 1
start_x = -pen1.xcor()
start_y = pen1.ycor() - 75

# Creating the Pen for the background
bg_pen = turtle.Turtle()
bg_pen.color("#e70000")
bg_pen.speed(10)
bg_pen.begin_fill()
bg_pen.penup()
bg_pen.goto(start_x-20-30, start_y+40)
bg_pen.pendown()
bg_pen.forward(590)
bg_pen.sety(bg_pen.ycor() - 180)
bg_pen.right(180)
bg_pen.forward(590)
bg_pen.right(90)
bg_pen.forward(180)
bg_pen.end_fill()
bg_pen.hideturtle()

# Creating Pen 2
pen2 = turtle.Turtle()

pen2.penup()
pen2.speed(0)
pen2.pensize(2)
pen2.goto(start_x, start_y)

# A
pen2.pendown()
pen2.goto(pen2.xcor()-30, pen2.ycor()-80)
pen2_temp1_x = pen2.xcor() + 15
pen2_temp1_y = pen2.ycor() + 40
pen2.goto(pen2.xcor()+30, pen2.ycor()+80)
pen2.goto(pen2.xcor()+30, pen2.ycor()-80)
pen2_temp2_x = pen2.xcor()
pen2.goto(pen2.xcor() - 15, pen2.ycor() + 40)
pen2.setheading(90)
pen2.goto(pen2_temp1_x, pen2_temp1_y)
pen2.right(90)
pen2.penup()

# I
pen2.forward(90)
pen2.pendown()
pen2.sety(pen2.ycor()-40)
pen2.sety(pen2.ycor()+80)
pen2.forward(30)
pen2.setheading(180)
pen2.forward(60)
pen2.penup()
pen2.sety(pen2.ycor()-80)
pen2.right(90)
pen2.pendown()
pen2.setx(pen2.xcor() + 60)
pen2.penup()

# L
pen2.setx(pen2.xcor()+75)
pen2.pendown()
pen2.setx(pen2.xcor()-60)
pen2.right(90)
pen2.sety(pen2.ycor()+80)
pen2.penup()

# P
pen2.forward(100)
pen2.pendown()
pen2.forward(40)
pen2.right(90)
pen2.forward(35)
pen2.right(90)
pen2.forward(40)
pen2.right(90)
pen2.forward(35)
pen2.backward(80)
pen2.penup()

# r
pen2.right(90)
pen2.forward(50)
pen2.pendown()
pen2.forward(5)
pen2.backward(2.5)
pen2.left(90)
pen2.forward(40)
pen2.right(90)
pen2.forward(35)
pen2.penup()

# o
pen2.forward(15)
pen2.pendown()
for i in range(4):
    pen2.forward(35)
    pen2.right(90)
pen2.penup()

# j
pen2.forward(60)
pen2.pendown()
pen2.setheading(270)
pen2.forward(80)
pen2.goto(pen2.xcor() - 20, pen2.ycor()+20)
pen2.penup()
pen2.goto(pen2.xcor() + 20, pen2.ycor()-20)
pen2.backward(95)
pen2.left(90)
pen2.forward(2.5)
pen2.pendown()
for i in range(4):
    pen2.right(90)
    pen2.forward(5)
pen2.penup()

# e
pen2.right(90)
pen2.forward(50)
pen2.left(90)
pen2.forward(15+40)
pen2.pendown()
pen2.backward(40)
pen2.left(90)
pen2.forward(35)
pen2.right(90)
pen2.forward(35)
pen2.right(90)
pen2.forward(15)
pen2.right(90)
pen2.forward(35)
pen2.penup()

# c
pen2.right(90)
pen2.backward(20)
pen2.right(90)
pen2.forward(40+15+35)
pen2.pendown()
pen2.backward(35)
pen2.sety(pen2.ycor()+35)
pen2.left(90)
pen2.setx(pen2.xcor()+35)
pen2.penup()

# t
pen2.right(90)
pen2.forward(15)
pen2.pendown()
pen2.forward(10)
pen2.backward(5)
pen2.left(90)
pen2.forward(45)
pen2.goto(pen2.xcor()-10, pen2.ycor()-10)
pen2.goto(pen2.xcor()+10, pen2.ycor()+10)
pen2.right(180)
pen2.forward(80)
pen2.left(90)
pen2.forward(10)
pen2.penup()

# line
pen2.right(90)
pen2.penup()
pen2.forward(10)
pen2.pendown()
pen2.setx(pen2.xcor()-120)
pen2.penup()
pen2.right(90)
pen2.forward(45)
pen2.sety(pen2.ycor()-5)
pen2.right(90)
pen2.pendown()
pen2.setx(start_x-30)
pen2.penup()


# Making the border
pen2.pensize(4)
pen2.goto(pen2.xcor()+570, pen2.ycor()+15-65)
temp_for_making_box_x = pen2.xcor()
pen2.right(180)
pen2.pendown()
pen2.setx(start_x-30-20)  # we are subtracting 30 because start_x is the middle of the "A" and another 20 for the border
pen2.right(180)
pen2.forward(180)
pen2.left(180)
pen2.setx(temp_for_making_box_x)
pen2.forward(180)
pen2.penup()

# Making the computer
pen2.pensize(2)
# Monitor
pen2.left(90)
pen2.forward(150)
pen2.left(90)
pen2.forward(80)
pen2.right(90)
pen2.pendown()
pen2.color("grey")
pen2.begin_fill()
for i in range(4):
    pen2.forward(100)
    pen2.left(90)
pen2.end_fill()
pen2.color("black")
for i in range(4):
    pen2.forward(100)
    pen2.left(90)
pen2.penup()

pen2.forward(20)
pen2.left(90)
pen2.forward(20)
pen2.right(90)
pen2.pendown()
pen2.color("white")
pen2.begin_fill()
for i in range(4):
    pen2.forward(60)
    pen2.left(90)
pen2.end_fill()
pen2.color("black")
for i in range(4):
    pen2.forward(60)
    pen2.left(90)
pen2.penup()

# Keyboard
pen2.forward(20)
pen2.right(90)
pen2.forward(20)
pen2.pendown()
pen2.forward(30)
pen2.pensize(4)
pen2.left(90)
pen2.forward(100)
pen2.right(90)
pen2.forward(40)
pen2.right(90)
pen2.forward(200)
pen2.right(90)
pen2.forward(40)
pen2.right(90)
pen2.forward(200)
pen2.right(90)
pen2.forward(20)
pen2.right(90)
pen2.forward(200)
pen2.right(90)
pen2.backward(20)
for i in range(5):
    pen2.forward(40)
    pen2.right(90)
    pen2.forward(20)
    pen2.right(90)
    pen2.forward(40)
    pen2.left(90)
    pen2.forward(20)
    pen2.left(90)
pen2.penup()

# Mouse
pen2.goto(pen2.xcor()-80, pen2.ycor()+70)
pen2.pensize(2)
pen2.pendown()
pen2.backward(15)
pen2.right(90)
pen2.forward(115)
pen2.right(90)
pen2.forward(15)
pen2.pensize(3)
for i in range(4):
    pen2.forward(10)
    pen2.left(90)
for i in range(3):
    pen2.forward(10)
    pen2.right(90)

pen2.pensize(4)
pen2.forward(20)
pen2.right(90)
pen2.forward(40)
pen2.right(90)
pen2.forward(20)
pen2.right(90)
pen2.forward(40)
pen2.penup()

# Sub
pen2.goto(start_x, start_y-180)
pen2.pendown()
pen2.pensize(2)
pen2.left(90)
pen2.forward(30)
pen2.right(180)
pen2.sety(pen2.ycor()-30)
pen2.forward(30)
pen2.right(90)
pen2.forward(30)
pen2.right(90)
pen2.forward(30)
pen2.penup()
pen2.left(180)

pen2.goto(pen2.xcor()+40, pen2.ycor()+30)
pen2.pendown()
pen2.sety(pen2.ycor()-30)
pen2.forward(30)
pen2.left(90)
pen2.forward(30)
pen2.penup()

pen2.setx(pen2.xcor()+10)
pen2.pendown()
pen2.right(90)
pen2.sety(pen2.ycor()+30)
pen2.right(90)
pen2.forward(60)
pen2.left(90)
for i in range(3):
    pen2.forward(30)
    pen2.left(90)
pen2.penup()

# Colon
pen2.left(90)
pen2.forward(50)
pen2.pendown()
for i in range(4):
    pen2.forward(15)
    pen2.left(90)
pen2.penup()
pen2.right(90)
pen2.forward(30)
pen2.left(90)
pen2.pendown()
for i in range(4):
    pen2.forward(15)
    pen2.left(90)

# C
pen2.penup()
pen2.forward(50+20)
pen2.left(90)
pen2.pendown()
pen2.setx(pen2.xcor()-30)
pen2.forward(60)
pen2.right(90)
pen2.forward(30)
pen2.penup()

# Fullstop
pen2.goto(pen2.xcor()+15, pen2.ycor()-60)
pen2.pendown()
for i in range(4):
    pen2.forward(15)
    pen2.left(90)
pen2.penup()

# S
pen2.forward(25)
pen2.pendown()
pen2.forward(30)
pen2.left(90)
pen2.forward(30)
pen2.left(90)
pen2.forward(30)
pen2.right(90)
pen2.forward(30)
pen2.right(90)
pen2.forward(30)
pen2.penup()

# S
pen2.right(180)
pen2.goto(pen2.xcor()-240, pen2.ycor()-100)
pen2.pendown()
pen2.forward(30)
pen2.sety(pen2.ycor()-30)
pen2.left(270)
pen2.setx(pen2.xcor()+30)
pen2.backward(30)
pen2.left(90)
pen2.forward(30)
pen2.penup()

# Fullstop
pen2.right(180)
pen2.forward(40)
pen2.pendown()
for i in range(4):
    pen2.forward(15)
    pen2.left(90)
pen2.penup()

# T
pen2.forward(40)
pen2.pendown()
pen2.sety(pen2.ycor()+60)
pen2.left(90)
pen2.setx(pen2.xcor()-30)
pen2.setx(pen2.xcor()+60)
pen2.penup()

# Colon
pen2.goto(pen2.xcor()+20, pen2.ycor()-30)
pen2.left(270)
pen2.pendown()
for i in range(4):
    pen2.forward(15)
    pen2.left(90)
pen2.penup()
pen2.right(90)
pen2.forward(30)
pen2.left(90)
pen2.pendown()
for i in range(4):
    pen2.forward(15)
    pen2.left(90)
pen2.penup()

# S
pen2.forward(40)
pen2.pendown()
pen2.forward(30)
pen2.sety(pen2.ycor()+30)
pen2.left(270)
pen2.setx(pen2.xcor()-30)
pen2.backward(30)
pen2.left(90)
pen2.forward(30)
pen2.penup()

# h
pen2.forward(10)
pen2.pendown()
pen2.right(90)
pen2.forward(60)
pen2.backward(30)
pen2.left(90)
pen2.forward(30)
pen2.right(90)
pen2.forward(30)
pen2.penup()

# r
pen2.left(90)
pen2.forward(10)
pen2.pendown()
pen2.forward(5)
pen2.backward(2.5)
pen2.left(90)
pen2.forward(30)
pen2.right(90)
pen2.forward(25)
pen2.penup()

# u
pen2.forward(10)
pen2.pendown()
pen2.sety(pen2.ycor()-30)
pen2.forward(30)
pen2.left(90)
pen2.forward(30)
pen2.penup()

# t
pen2.right(90)
pen2.forward(10)
pen2.pendown()
pen2.forward(10)
pen2.backward(5)
pen2.left(90)
pen2.forward(30)
pen2.goto(pen2.xcor()-10, pen2.ycor()-10)
pen2.goto(pen2.xcor()+10, pen2.ycor()+10)
pen2.right(180)
pen2.forward(60)
pen2.left(90)
pen2.forward(10)
pen2.penup()

# i
pen2.forward(10)
pen2.pendown()
pen2.forward(5)
pen2.back(2.5)
pen2.left(90)
pen2.forward(30)
pen2.goto(pen2.xcor()-5, pen2.ycor()-5)
pen2.penup()
pen2.goto(pen2.xcor()+5, pen2.ycor()+5)
pen2.forward(5)
pen2.right(90)
pen2.pendown()
pen2.forward(2.5)
for i in range(4):
    pen2.left(90)
    pen2.forward(5)
pen2.penup()

# M
pen2.forward(40)
pen2.sety(pen2.ycor()-35)
pen2.pendown()
pen2.left(90)
pen2.forward(60)
pen2.goto(pen2.xcor()+22.5, pen2.ycor()-22.5)
pen2.goto(pen2.xcor()+22.5, pen2.ycor()+22.5)
pen2.back(60)
pen2.penup()

# a
pen2.right(90)
pen2.forward(40)
pen2.pendown()
pen2.back(30)
pen2.left(90)
pen2.forward(15)
pen2.right(90)
pen2.forward(30)
pen2.sety(pen2.ycor()-15)
pen2.sety(pen2.ycor()+30)
pen2.left(180)
pen2.forward(30)
pen2.penup()

# Ma'am
# '
pen2.setheading(0)
pen2.forward(40)
pen2.left(90)
pen2.forward(10)
pen2.pendown()
pen2.pensize(3)
pen2.forward(20)
pen2.pensize(2)
pen2.penup()

# a
pen2.back(60)
pen2.right(90)
pen2.forward(40)
pen2.pendown()
pen2.back(30)
pen2.left(90)
pen2.forward(15)
pen2.right(90)
pen2.forward(30)
pen2.sety(pen2.ycor()-15)
pen2.sety(pen2.ycor()+30)
pen2.left(180)
pen2.forward(30)
pen2.penup()

# m
pen2.right(180)
pen2.forward(47.5)
pen2.left(90)
pen2.pendown()
pen2.goto(pen2.xcor()-7.5, pen2.ycor()-7.5)
pen2.goto(pen2.xcor()+7.5, pen2.ycor()+7.5)
pen2.left(180)
pen2.forward(30)
pen2.backward(30)
pen2.setx(pen2.xcor()+20)
pen2.forward(30)
pen2.right(180)
pen2.forward(30)
pen2.setx(pen2.xcor()+20)
pen2.left(180)
pen2.forward(30)
pen2.penup()

# M
pen2.pensize(3)
pen2.goto(pen2.xcor()+160, pen2.ycor()+160)
pen2.pendown()
pen2.forward(20)
pen2.back(20)
pen2.goto(pen2.xcor()+10, pen2.ycor()-10)
pen2.goto(pen2.xcor()+10, pen2.ycor()+10)
pen2.right(90)
pen2.sety(pen2.ycor()-20)
pen2.penup()

# a
pen2.right(180)
pen2.forward(5)
pen2.pendown()
pen2.forward(10)
pen2.back(10)
pen2.left(90)
pen2.forward(5)
pen2.right(90)
pen2.forward(10)
pen2.sety(pen2.ycor()-5)
pen2.sety(pen2.ycor()+10)
pen2.left(180)
pen2.forward(10)
pen2.penup()

# d
pen2.right(180)
pen2.goto(pen2.xcor()+15, pen2.ycor()-10)
pen2.pendown()
for i in range(4):
    pen2.forward(10)
    pen2.left(90)
pen2.forward(10)
pen2.left(90)
pen2.forward(20)
pen2.penup()

# e
pen2.right(90)
pen2.goto(pen2.xcor()+5, pen2.ycor()-10)
pen2.pendown()
pen2.forward(10)
pen2.right(90)
pen2.forward(5)
pen2.right(90)
pen2.forward(10)
pen2.left(180)
pen2.sety(pen2.ycor()+5)
pen2.sety(pen2.ycor()-10)
pen2.forward(10)
pen2.penup()

# b
pen2.forward(10)
pen2.pendown()
for i in range(4):
    pen2.forward(10)
    pen2.left(90)
pen2.left(90)
pen2.forward(20)
pen2.penup()

# y
pen2.goto(pen2.xcor()+15, pen2.ycor()-10)
pen2.pendown()
pen2.right(90)
pen2.goto(pen2.xcor()+5, pen2.ycor()-10)
pen2.goto(pen2.xcor()+5, pen2.ycor()+10)
pen2.goto(pen2.xcor()-10, pen2.ycor()-20)
pen2.pensize(2)
pen2.penup()

#

# S
pen2.goto(pen2.xcor()-125, pen2.ycor()-95)
pen2.pensize(3)
pen2.pendown()
pen2.forward(15)
pen2.back(15)
pen2.right(90)
pen2.forward(15)
pen2.left(90)
pen2.forward(15)
pen2.right(90)
pen2.forward(15)
pen2.right(90)
pen2.forward(15)
pen2.left(180)
pen2.penup()

# r
pen2.forward(20)
pen2.pendown()
pen2.left(90)
pen2.forward(15)
pen2.back(2.5)
pen2.right(90)
pen2.forward(12.5)
pen2.penup()

# ee
pen2.goto(pen2.xcor()+5, pen2.ycor()+2.5)
for i in range(2):
    pen2.pendown()
    pen2.forward(15)
    pen2.right(90)
    pen2.forward(7.5)
    pen2.right(90)
    pen2.forward(15)
    pen2.left(180)
    pen2.sety(pen2.ycor()+7.5)
    pen2.sety(pen2.ycor()-15)
    pen2.forward(15)
    pen2.penup()
    pen2.goto(pen2.xcor()+5, pen2.ycor()+15)
pen2.penup()

# d
pen2.forward(5)
pen2.pendown()
for i in range(4):
    pen2.forward(15)
    pen2.right(90)
pen2.forward(15)
pen2.left(180)
pen2.sety(pen2.ycor()+15)
pen2.right(180)
pen2.penup()

# e
pen2.goto(pen2.xcor()+5, pen2.ycor()-15)
pen2.pendown()
pen2.forward(15)
pen2.right(90)
pen2.forward(7.5)
pen2.right(90)
pen2.forward(15)
pen2.left(180)
pen2.sety(pen2.ycor()+7.5)
pen2.sety(pen2.ycor()-15)
pen2.forward(15)
pen2.penup()

# v
pen2.forward(12.5)
pen2.left(90)
pen2.pendown()
pen2.goto(pen2.xcor()-7.5, pen2.ycor()+15)
pen2.goto(pen2.xcor()+7.5, pen2.ycor()-15)
pen2.goto(pen2.xcor()+7.5, pen2.ycor()+15)
pen2.penup()

# Fullstop
pen2.setheading(0)
pen2.goto(pen2.xcor()+10, pen2.ycor()-7.5)
pen2.pendown()
for i in range(4):
    pen2.forward(7.5)
    pen2.right(90)
pen2.penup()

# N
pen2.goto(pen2.xcor()+10+7.5, pen2.ycor()-7.5)
pen2.pendown()
pen2.left(90)
pen2.forward(30)
pen2.right(90)
pen2.goto(pen2.xcor()+15, pen2.ycor()-30)
pen2.left(90)
pen2.forward(30)
pen2.penup()

# Sign
# S
pen2.forward(50)
pen2.left(90)
pen2.forward(10)
pen2.left(15)
pen2.pensize(2)
pen2.pendown()
pen2.forward(140)
pen2.setheading(15)
for i in range(21):
    pen2.left(15)
    pen2.forward(7.5)
pen2.left(95)
pen2.forward(40)
for i in range(9):
    pen2.left(36)
    pen2.forward(5)
pen2.right(40)
pen2.forward(10)
pen2.right(60)
pen2.forward(15)
pen2.right(45)
pen2.forward(16)
pen2.right(45)
pen2.forward(10)
pen2.right(60)
pen2.forward(20)
pen2.penup()
# r
pen2.goto(pen2.xcor()+40, pen2.ycor()-7)
pen2.pendown()
pen2.setheading(45+15)
pen2.forward(25)
for i in range(10):
    pen2.left(36)
    pen2.forward(2.5)
pen2.back(5)
pen2.setheading(0+15)
pen2.forward(15)
pen2.setheading(230+15)
pen2.forward(20)
# e
pen2.setheading(0+15)
pen2.forward(10)
pen2.left(45)
pen2.forward(25)
pen2.right(160)
pen2.forward(20)
# e
pen2.setheading(0+15)
pen2.forward(10)
pen2.left(45)
pen2.forward(25)
pen2.right(160)
pen2.forward(20)
# d
pen2.setheading(0+15)
pen2.forward(25)
pen2.left(90)
pen2.forward(10)
for i in range(10):
    pen2.left(36)
    pen2.forward(5)
pen2.right(20)
pen2.forward(35)
pen2.back(45)
# e
pen2.setheading(0+15)
pen2.forward(5)
pen2.left(45)
pen2.forward(25)
pen2.right(160)
pen2.forward(20)
# v
pen2.setheading(0+15)
pen2.forward(5)
pen2.left(45)
pen2.forward(25)
pen2.right(160)
pen2.forward(20)
pen2.setheading(0+15)
pen2.left(45)
pen2.forward(25)
pen2.hideturtle()


turtle.done()  # We are using this program so that when the turtle has finished its program, the window will not get closed immediately

'''
Further explanation/documentation will be on my GitHub account : Sreedev123
'''