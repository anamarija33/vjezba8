'''
1.	Napišite program kolokvij2_zd01.py koji od korisnika traži unos cijelog broja n većeg od 0 (potrebno je napraviti provjeru),
 te potom generira n listi od kojih se svaka sastoji od 5 nasumičnih (random) prirodnih brojeva između 0 i 10. Program potom treba 
 ispisati onu listu kod koje je suma svih elemenata liste najveća.
Npr. za n = 3 jedan mogući ispis bi bio (ako su generirane liste [0, 5, 3, 1, 6], [10, 1, 2, 0, 1],
[3, 2, 3, 9, 9]):
lista_s_najvecom_sumom = [3, 2, 3, 9, 9]
'''
import random
n = int(input("Upiši cili broj veći od 0: "))
if n>0:
    liste = []
    sume = []
    for i in range(5):
        liste.append([])
        for j in range(5):
            liste[i].append(random.randint(0,10))
        sume.append(sum(liste[i]))
maximum = max(sume)
lista_s_najvecom_sumom = liste[sume.index(maximum)]
print("lista s najvećom sumom: ",lista_s_najvecom_sumom)

