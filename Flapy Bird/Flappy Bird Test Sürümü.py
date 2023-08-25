import turtle, time, random

print("SANA BU DOSYAYI AÇMA DEMİŞTİM AMA HER NEYSE")



puan1 = 0



pencere = turtle.Screen()
canvas = pencere.getcanvas()
root = canvas.winfo_toplevel()
pencere.title('Flappy Bird - Gevşek Kuş')
pencere.bgcolor('blue')
pencere.bgpic('background2.gif')
pencere.setup(width=500, height=700)
pencere.tracer(0)

pencere.register_shape('bird.gif')

bird = turtle.Turtle()
bird.speed(0)
bird.color('yellow')
bird.shape('bird.gif')
bird.penup()
bird.goto(-180, 0)
bird.dx = 0
bird.dy = 1

puan = 100
yaz = turtle.Turtle()
yaz.speed(0)
yaz.color('white')
yaz.shape('square')
yaz.hideturtle()
yaz.penup()
yaz.goto(0, 300)
yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'bold'))

yaz1 = turtle.Turtle()
yaz1.speed(0)
yaz1.color('red')
yaz1.shape('square')
yaz1.hideturtle()
yaz1.penup()
yaz1.goto(0, 250)


yercekimi = -0.3

def bird_up(x, y):
    bird.dy = bird.dy + 8

    if bird.dy > 8:
        bird.dy = 8

def kapat():
    global devam
    devam = False
    exit()

borular = []
pencere.listen()
pencere.onscreenclick(bird_up)
root.protocol("WM_DELETE_WINDOW", kapat)
devam = True

starting_time = time.time()
while devam:
    time.sleep(0.02)
    pencere.update()
    yaz1.clear()
    yaz1.write('Geçilen Engel: {}'.format(puan1), align='center', font=('Courier', 24, 'bold'))
    yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'bold'))
    if puan1 >= 10:
        yaz1.color("orange")
    if puan1 >= 20:
        yaz1.color("yellow")
    if puan1 >= 30:
        yaz1.color("lightgreen")
    if puan1 >= 40:
        yaz1.color("green")
    if puan == 100:
        yaz.color("green")
    if puan <= 80:
        yaz.color("lightgreen")
    if puan <= 60:
        yaz.color("yellow")
    if puan <= 40:
        yaz.color("orange")       
    if puan <= 20:
        yaz.color("red")
    if puan == 0:
        yaz.color("white")







    bird.dy = bird.dy + yercekimi

    if (time.time() - starting_time > random.randint(5, 15)):
        starting_time = time.time()
        boru_ust = turtle.Turtle()
        boru_ust.speed(100)
        boru_ust.color('red')
        boru_ust.shape('square')
        boru_ust.h = random.randint(10, 20)
        boru_ust.shapesize(boru_ust.h, 2, outline=None)
        boru_ust.penup()
        boru_ust.goto(300, 250)
        boru_ust.dx = -2
        boru_ust.dy = 0

        boru_alt = turtle.Turtle()
        boru_alt.speed(100)
        boru_alt.color('red')
        boru_alt.shape('square')
        boru_alt.h = 40 - boru_ust.h - random.randint(1, 10)
        boru_alt.shapesize(boru_alt.h, 2, outline=None)
        boru_alt.penup()
        boru_alt.goto(300, -250)
        boru_alt.dx = -2
        boru_alt.dy = 0

        borular.append((boru_ust, boru_alt))


    y = bird.ycor()
    y = y + bird.dy
    bird.sety(y)

    if len(borular) > 0:
        for boru in borular:
            x = boru[0].xcor()
            x = x + boru[0].dx
            boru[0].setx(x)
            x = boru[1].xcor()
            x = x + boru[1].dx
            boru[1].setx(x)
            if boru[0].xcor() < -300:
                boru[0].hideturtle()
                boru[1].hideturtle()
                borular.pop(borular.index((boru)))
            if (bird.xcor()+10>boru[0].xcor()-20) and (bird.xcor()-10<boru[0].xcor()+20):
                if (bird.ycor()+10>boru[0].ycor()-boru[0].h*10) or (bird.ycor()-10<boru[1].ycor()+boru[1].h*10):
                    puan = puan - 1
                    yaz.clear()
                    yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'bold'))
                else:
                    puan1 = puan1 + 1
                    
                        
                        
                    

    if puan < 0:
        pencere.bgpic("background3.gif")
        yaz.clear()
        yaz1.clear()
        yaz1.color("red")
        yaz.color("red")
        yaz.write('Kaybettiniz', align='center', font=('Courier', 24, 'bold'))
        yaz1.write('Kaybettiniz', align='center', font=('Courier', 24, 'bold'))
        print("")
        print("BAK SANA AÇMA DEMİŞTİM AMA SEN AÇMAYI TERCİH ETTİN GÖRÜŞÜRÜZ :) :D")
        exit()

            
            

