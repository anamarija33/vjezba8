'''
1. Napišite program vjezba11_zd01.py koji od korisnika traži unos cijelog broja n većeg od 0
(potrebno je napraviti provjeru), te generira i ispisuje listu od n nasumičnih (random)
prirodnih brojeva između 1 i 100. Potom treba prebrojati i ispisati koliko u toj listi ima
parnih, a koliko neparnih brojeva.
Npr. za n = 5 jedan mogući ispis bi bio:
Polazna_lista=[6, 31, 75, 3, 42]
U listi ima 2 parnih i 3 neparnih brojeva.
'''
import random
n = int(input("Upiši cili broj veći od 0: "))
brojevi = []
if n>0:
    for i in range(n):
         brojevi.append(random.randint(1,101))

    parni = [i for i in brojevi if i%2==0]
    neparni = [i for i in brojevi if i%2!=0]
    print("Polazna lista = ",brojevi)
    print("U listi ima",len(parni),"parnih, i",len(neparni),"neparnih brojeva.")
else:
    print("Krivi unos")
