import turtle
import time

hiz = 0.15

pencere = turtle.Screen()
canvas = pencere.getcanvas()
root = canvas.winfo_toplevel()


def kapat():
    global devam
    devam = False
    exit()



root.protocol("WM_DELETE_WINDOW", kapat)

devam = True
while devam:
    pencere.bgcolor("green")
    print("Yeşil")
    time.sleep(hiz)
    pencere.bgcolor("blue")
    print("Mavi")
    time.sleep(hiz)
    pencere.bgcolor("red")
    print("Kırmızı")
    time.sleep(hiz)
    pencere.bgcolor("yellow")
    print("Sarı")
    time.sleep(hiz)
    pencere.bgcolor("lightblue")
    print("Açık Mavi")
    time.sleep(hiz)
    pencere.bgcolor("black")
    print("Siyah")
    time.sleep(hiz)
    pencere.bgcolor("white")
    print("Beyaz")
    time.sleep(hiz)
    pencere.bgcolor("purple")
    print("Mor")
    time.sleep(hiz)
    pencere.bgcolor("pink")
    print("Pembe")
    time.sleep(hiz)
    pencere.bgcolor("brown")
    print("Kahverengi")
    time.sleep(hiz)
    pencere.bgcolor("lightgreen")
    print("Açık Yeşil")
    time.sleep(hiz)
    pencere.bgcolor("gray")
    print("Gri")
    time.sleep(hiz)
    pencere.bgcolor("tomato")
    print("Domates Kırmızısı")
    time.sleep(hiz)
    pencere.bgcolor("cyan")
    print("Turkuaz")
    time.sleep(hiz)
    pencere.bgcolor("magenta")
    print("Eflatun")
    time.sleep(hiz)
    pencere.bgcolor("gold")
    print("Altın Sarısı")
    time.sleep(hiz)
