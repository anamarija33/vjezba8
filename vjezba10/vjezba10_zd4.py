'''
Napišite program vjezba10_zd04.py koji od korisnika traži unos cijelog broja n (n>2), te crta
pravilni n-terokut kojemu je opisana kružnica radijusa 200 piksela sa središtem u ishodištu
ekrana (0, 0).
'''
from turtle import *
broj = int(input("broj : "))
kut = 360/broj
stranica = 10
for i in range(broj):
    fd(stranica)
    left(kut)
    write(str(i+1))
