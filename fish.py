#initial
import turtle

##turtle name is jel bc i am too lazy to type "anjelica" every time I call the turtle
jel = turtle.Turtle()
jel.pensize(10)
#Angelo Talamonti
#9/10/2024

import turtle
angelo = turtle.Turtle()
angelo.pensize(10)



#function


#makes the outline of the fishbody
#coded by: Anjelica
def fishbody():
    jel.penup()
    jel.goto(100,0)
    jel.seth(120)
    jel.circle(300,18)
    jel.pd()
    jel.circle(300,102)
    jel.left(20)
    jel.forward(10)
    jel.circle(20,100)
    jel.left(200)
    jel.circle(20,100)
    jel.seth(330)
    for i in range(3):
        jel.circle(300,30)
        jel.right(15)
    jel.circle(300,15)

#makes the shape of the tail
#coded by: Anjelica
def fishtail():
    jel.pu()
    jel.seth(0)
    jel.forward(20)
    jel.seth(140)
    jel.pd()
    jel.circle(20,90)
    jel.pu()
    jel.seth(0)
    jel.forward(20)
    jel.pd()
    jel.forward(50)
    jel.left(40)
    jel.circle(100,100)
    jel.seth(200)
    jel.forward(150)

#makes the stripe between the tail and body
#coded by: Anjelica
def backstripe():
    for i in range(3):
        jel.circle(50,60)
        jel.right(20)
        jel.forward(5)
    jel.pu()
    jel.goto(35,75)
    jel.pd()
    jel.seth(270)
    jel.forward(150)

#makes the curvey middle stripe in the clownfish
#coded by: Anjelica
def middlestripe():
    jel.pu()
    jel.goto(-50,120)
    jel.seth(230)
    jel.pd()
    jel.circle(180,75)
    jel.pu()
    jel.goto(-200,150)
    jel.pd()
    jel.seth(180)
    jel.circle(50,-130)
    jel.left(150)
    jel.circle(60,130)
    jel.seth(200)
    jel.circle(40,-180)

#makes top back fin
#coded by: Anjelica
def topbackfin():
    jel.pu()
    jel.goto(40,80)
    jel.seth(250)
    jel.pd()
    jel.circle(20,-50)
    jel.seth(120)
    jel.forward(50)
    jel.circle(30,90)
    jel.forward(40)


#draws eye of fish
#coded by: Angelo
def eye():
    angelo.pu()
    angelo.goto(-350,25)
    angelo.pd()
    angelo.seth(180)
    angelo.circle(25)
    angelo.circle(15)
#draws fin of fish
#coded by: Angelo
def fin():
    angelo.pu()
    angelo.goto(-200,-50)
    angelo.pd()
    angelo.seth(0)
    angelo.forward(50)
    angelo.right(120)
    angelo.forward(100)
    angelo.right(110)
    angelo.forward(50)
#draws top fin of fish
#coded by: Angelo
def top():
    angelo.pu()
    angelo.goto(-100,150)
    angelo.pd()
    angelo.seth(90)
    angelo.circle(75,190)
#draws bottom fin of fish
#coded by: Angelo
def bottom():
    angelo.pu()
    angelo.goto(-250,-100)
    angelo.pd()
    angelo.seth(270)
    angelo.circle(30,180)
#draws left front stripe
#coded by: Angelo
def frontStripe():
    angelo.pu()
    angelo.goto(-300,-100)
    angelo.pd()
    angelo.left(30)
    angelo.circle(100,150)


#draws left front stripe
#coded by: Angelo
def frontStripe2():
    angelo.pu()
    angelo.goto(-300,120)
    angelo.pd()
    angelo.circle(110,-160)
#draws bubbles next to fish
#coded by: Angelo
def bubbles():
    angelo.left(90)
    angelo.pu()
    angelo.goto(-475,35)
    for i in range(3):
        angelo.circle(10)
        angelo.penup()
        angelo.backward(40)
        angelo.pendown()
#draws bottom back fin
#coded by: Angelo
def bottombackFin():
    angelo.pu()
    angelo.goto(-100,-100)
    angelo.pd()
    angelo.seth(270)
    angelo.circle(35,100)
    angelo.forward(60)
    angelo.circle(25,120)







#main

fishbody()
fishtail()
jel.backward(100)
backstripe()
middlestripe()
topbackfin()
frontStripe()
frontStripe2()
bubbles()
fin()
top()
bottom()
eye()
bottombackFin()

