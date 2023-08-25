#TürkBayrağı##15TEMMUZ##00:34#

import turtle

ayyildiz = turtle.Turtle()
ekran=turtle.Screen()
ekran.title("TÜRKBAYRAĞI")
ekran.bgcolor("red")

ayyildiz.penup()
ayyildiz.setposition(-50,-150)
ayyildiz.begin_fill()
ayyildiz.pendown()
ayyildiz.color("white")
ayyildiz.circle(150)
ayyildiz.end_fill()

ayyildiz.penup()
ayyildiz.setposition(0,-120)
ayyildiz.begin_fill()
ayyildiz.pendown()
ayyildiz.color("red")
ayyildiz.circle(120)
ayyildiz.end_fill()

ayyildiz.penup()
ayyildiz.color("white")
ayyildiz.setposition(85,65)
ayyildiz.pendown()
ayyildiz.right(55)
ayyildiz.begin_fill()

for i in range(5):
    ayyildiz.forward(130)
    ayyildiz.right(144)

ayyildiz.penup()
ayyildiz.setposition(131,-1)
ayyildiz.pendown()

for i in range(5):
    ayyildiz.right(72)
    ayyildiz.forward(30)

ayyildiz.end_fill()
ayyildiz.hideturtle()
ekran.exitonclick()
