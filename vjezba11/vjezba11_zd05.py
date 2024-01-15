'''
5. Napišite program vjezba11_zd05.py koji od korisnika traži unos prirodnog broja n manjeg od
50 (0<n<50), te potom pomoću modula turtle.py iscrtava 5 jednakostraničnih trokuta sa
jednim zajedničkim vrhom, tako da je je duljina stranice prvog trokuta 300 piksela, a duljina
stranice svakog idućeg trokuta za n piksela manja od prethodnog, i da je svaki trokut ispunjen
sa nekom proizvoljnom nijansom sive boje. Npr. za n = 30 program može iscrtati sljedeće:
'''
import turtle
t = turtle.Turtle()

n = int(input("Upiši n tako da je 0<n<50: "))
if n > 0 and n < 50:
    s = 300
    col = 8
    for i in range(5):
        t.fillcolor(col/255,col/255,col/255)
        t.begin_fill()
        for i in range(3):
            t.forward(s)
            t.right(120)
        t.end_fill()
        col*=2
        s-=n

else: 
    print("krivi unos")