'''
4. Napišite program vjezba10_zd04.py koji od korisnika traži unos cijelog broja n (n>2), te crta
pravilni n-terokut kojemu je opisana kružnica radijusa 200 piksela sa središtem u ishodištu
ekrana (0, 0).'''


from turtle import *
broj = int(textinput("Upis broja","Upiši broj veći od 2"))

if broj>2:
    right(90)
    penup()
    forward(200)
    pd()
    left(90)
    circle(200,360)
    circle(200,360,broj)