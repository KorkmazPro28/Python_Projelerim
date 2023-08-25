import random
import turtle
import time
delay = 0.15

pencere = turtle.Screen()
canvas = pencere.getcanvas()
root = canvas.winfo_toplevel()
pencere.title('Yılan Oyunu')
pencere.bgcolor('cyan')
pencere.setup(width=600, height=600)
pencere.tracer(0)

kafa = turtle.Turtle()
kafa.speed(100)
kafa.shape("square")
kafa.color("black")
kafa.penup()
kafa.goto(0, 100)
kafa.direction = "stop"

yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("circle")
yemek.color("green")
yemek.penup()
yemek.shapesize(0.80, 0.80)
yemek.goto(0, 0)

yemek2 = turtle.Turtle()
yemek2.speed(0)
yemek2.shape("circle")
yemek2.color("red")
yemek2.penup()
yemek2.shapesize(0.80, 0.80)
yemek2.goto(1000, 1000)

yemek3 = turtle.Turtle()
yemek3.speed(0)
yemek3.shape("circle")
yemek3.color("yellow")
yemek3.penup()
yemek3.shapesize(0.80, 0.80)
yemek3.goto(1000, 1000)

kuyruklar = []
puan = 0
sayi = 100

yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape("square")
yaz.color("black")
yaz.penup()
yaz.hideturtle()
yaz.goto(0, 260)
yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))

def move():
    if kafa.direction == "up":
        y = kafa.ycor()
        kafa.sety(y + 20)
    if kafa.direction == "down":
        y = kafa.ycor()
        kafa.sety(y - 20)
    if kafa.direction == "right":
        x = kafa.xcor()
        kafa.setx(x + 20)
    if kafa.direction == "left":
        x = kafa.xcor()
        kafa.setx(x - 20)

        
def go_up():
    if kafa.direction != "down":
        kafa.direction = "up"

        
def go_down():
    if kafa.direction != "up":
        kafa.direction = "down"





def go_right():
    if kafa.direction != "left":
        kafa.direction = "right"

def go_left():
    if kafa.direction != "right":
        kafa.direction = "left"

        
def kapat():
    devam = False
    exit()

pencere.listen()
root.protocol("WM_DELETE_WINDOW", kapat)
pencere.onkey(go_up, "Up")
pencere.onkey(go_down, "Down")
pencere.onkey(go_right, "Right")
pencere.onkey(go_left, "Left")

devam = True
while devam:
    pencere.update()
    if puan >= sayi:
        puan = 100
        kafa.goto(0,0)
        kafa.direction = "stop"
        yeni_kuyruk.goto(1000, 1000)
        yaz.clear()
        yaz.write("Kazandınız",align="center", font=("Courier", 24, "normal"))
        time.sleep(1)
        yaz.clear()
        yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))    
        x3 = random.randint(-250, 250)
        y3 = random.randint(-250, 250)
        yemek2.goto(x3,y3)
        sayi = 200
    if puan >= sayi:
        print("Bir Sonraki Güncelleme Yakında :D")
        exit()
        #puan = 100
        #kafa.goto(0,0)
        #kafa.direction = "stop"
        #yeni_kuyruk.goto(1000, 1000)
        #yaz.clear()
        #yaz.write("Kazandınız",align="center", font=("Courier", 24, "normal"))
        #time.sleep(1)
        #yaz.clear()
        #yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))    
        #x4 = 0
        #y4 = 100
        #yemek3.goto(x4,y4)
        #sayi = 300    
   

    



    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300:
        time.sleep(1)
        kafa.goto(0, 0)
        kafa.direction = "stop"

        for kuyruk in kuyruklar:
            kuyruk.goto(1000, 1000)
        kuyruklar = []

        puan = 0
        delay = 1.0

        yaz.clear()
        yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))

    if kafa.distance(yemek) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek.goto(x, y)

        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape("square")
        yeni_kuyruk.color("white")
        yeni_kuyruk.penup()
        kuyruklar.append(yeni_kuyruk)

        delay -= 0.001

        puan = puan + 10
        yaz.clear()
        yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
        
    if kafa.distance(yemek2) < 20:
        x2 = random.randint(-250, 250)
        y2 = random.randint(-250, 250)
        yemek2.goto(x2, y2)

        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape("square")
        yeni_kuyruk.color("white")
        yeni_kuyruk.penup()
        kuyruklar.append(yeni_kuyruk)

        delay -= 0.001

        puan = puan + 10
        yaz.clear()
        yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
        
    if kafa.distance(yemek3) < 20:
        x4 = random.randint(-250, 250)
        y4 = random.randint(-250, 250)
        yemek3.goto(x4, y4)

        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape("square")
        yeni_kuyruk.color("white")
        yeni_kuyruk.penup()
        kuyruklar.append(yeni_kuyruk)

        delay -= 0.001

        puan = puan + 10
        yaz.clear()
        yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
        
    for index in range(len(kuyruklar) - 1, 0, -1):
        x = kuyruklar[index - 1].xcor()
        y = kuyruklar[index - 1].ycor()
        kuyruklar[index].goto(x, y)

    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x, y)

    move()

    for segment in kuyruklar:
        if segment.distance(kafa) < 20:
            time.sleep(1)
            kafa.goto(0, 0)
            kafa.direction = "stop"
            for segment in kuyruklar:
                segment.goto(1000, 1000)
            kuyruklar = []
            puan = 0
            yaz.clear()
            yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))
            hiz = 0.15

    time.sleep(delay)

