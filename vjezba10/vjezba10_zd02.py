'''
2. Napišite program vjezba10_zd02.py koji od korisnika traži unos duljine stranice kvadrata, te
pozivom funkcije kvadrat(duljina) crta kvadrat sa stranicom duljine duljina koju je korisnik
prethodno unio (duljina mora biti veća od 0).
'''

from turtle import * 


def kvadrat (duljina):
    for i in range(4):
        fd(duljina)
        right(90)
duljina = int(input("Unesi duljinu stranice kvadrata: "))
if duljina> 0:
    kvadrat(duljina)

else:
    print("pogrešan unos.")