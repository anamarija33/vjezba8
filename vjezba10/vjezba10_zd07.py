'''
7. Napišite program vjezba10_zd07.py koji po ekranu iscrtava n nasumično (random)
raspoređenih točaka radijusa m piksela, te pritom ispod svake od njih ispisuje uređeni par
koordinata pripadne točke (x, y) pri čemu su x i y koordinate točke. Svaku točku treba obojati
nasumičnom bojom, a koordinate trebaju biti ispisane crnom bojom. Brojeve n i m treba
unijeti korisnik na početku izvođenja programa pomoću funkcije textinput(prompt, message).
'''
from turtle import *
import random
n = int(textinput("Broj n", "upiši broj n: "))
m = int(textinput("Broj n", "upiši broj n: "))
def gen_col():
    r = random.randint(1,255)/255
    g = random.randint(1,255)/255
    b = random.randint(1,255)/255
    return r,g,b
def gen_coord():
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    return x,y
def draw():
    x,y = gen_coord()
    goto(x,y)
    pd()
    begin_fill()
    circle(m,360)
    end_fill()
    pu()
    write((x,y),move=True)


pu()
for i in range(n):
    r,g,b = gen_col()
    fillcolor(r,g,b)
    draw()

    