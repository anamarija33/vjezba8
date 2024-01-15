'''
6. (Bonus zadatak) Napišite program vjezba11_zd06.py koji simulira igru Loto 7/39 na način da
od korisnika traži unos 7 različitih prirodnih brojeva između 1 i 39 (pri čemu se svaki broj
unosi zasebno u novoj liniji, a ukoliko se unese nedozvoljeni broj (manji od 1 ili veći od 39) ili
se ponovi već uneseni broj, program mora javiti pogrešku i ponovno tražiti unos tog broja).
Također, treba omogućiti da u bilo kojem trenutku korisnik može izaći iz programa tako da
unese 0 (nulu). Nakon što korisnik unese 7 različitih brojeva, program treba pozvati funkciju
izvlacenje_brojeva() unutar koje se generira druga lista od 7 nasumičnih (random) brojeva
između 1 i 39 (ta se lista vraća kao povratna vrijednost funkcije), te se pomoću funkcije
usporedi(lista1, lista2) provjerava koliko se brojeva koje je korisnik unio u lista1 nalazi u listi
nasumično generiranih brojeva lista2 (kao kod izvlačenja lota 7/39). Ako korisnik pogodi svih
7 brojeva, program treba ispisati poruku 'JACKPOT', a u protivnom ispisati koliko je brojeva
pogođeno.
Npr. za unesenu listu [2, 13, 21, 23, 32, 33, 39] program generira nasumičnu listu
[31, 2, 27, 33, 4, 9, 13] i ispisuje poruku da je pogođeno 3 broja'''
import random
lista = []
brojcanik = 0
while(brojcanik!= 7):
    broj = int(input("Upiši broj između 1 i 39: "))
    if broj >= 1 and broj <=39 and broj not in lista:
        lista.append(broj)
        brojcanik+=1
def izvlacenje_brojeva():
    nasumicni = []
    for i in range(7):
        nasumicni.append(random.randint(1,40))
    return nasumicni
lista2= izvlacenje_brojeva()
print(lista,lista2)
def usporedi(lista,lista2):
    br = 0
    for i in lista:
        if i in lista2:
            br+=1
    if br == 7:
        print("JACKPOT")

    else:
        print(br,'pogođeno.')
usporedi(lista,lista2)
        
        