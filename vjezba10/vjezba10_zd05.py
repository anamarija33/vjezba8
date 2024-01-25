'''
5. Napišite program vjezba10_zd05.py koji crta isto što i prethodni program, samo što kružnica
mora biti ispunjena crvenom bojom, a upisani n-terokut plavom bojom.
'''

from turtle import *
broj = int(textinput("Upis broja","Upiši broj veći od 2"))

if broj>2:
    right(90)
    penup()
    forward(200)
    pd()
    left(90)
    fillcolor("red")
    begin_fill()
    circle(200,360)
    end_fill()
    fillcolor("blue")
    begin_fill()
    circle(200,360,broj)
    end_fill()