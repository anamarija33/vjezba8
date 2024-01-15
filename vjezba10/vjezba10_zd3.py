'''
Napišite program vjezba10_zd03.py koji od korisnika traži unos cijelog broja n (n>2), te crta
pravilni n-terokut sa stranicom duljine 100 piksela, pri čemu se svaki vrh označava brojem (od
1 do n).

'''
from turtle import *
broj = int(input("Upiši veći broj od 2: "))
kut = 360/broj
stranica = 100
for i in range(broj):
    fd(stranica)
    left(kut)
    write(str(i+1))