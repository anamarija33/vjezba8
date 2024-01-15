'''
2. Napišite program vjezba11_zd02.py koji korištenjem funkcije samoglasnici(s) ispituje koliko u
zadanom nizu znakova s postoji samoglasnika. Niz znakova treba unijeti korisnik, a glavni
program potom treba pozvati funkciju samoglasnici(s) sa zadanim stringom kao
argumentom, te u ovisnosti o povratnoj vrijednosti funkcije ispisati koliko u zadanom stringu
ima samoglasnika, te koliki je postotak samoglasnika u odnosu na ukupnu duljinu stringa.
Npr. za ulazni string s='Ovo je primjer.' program može izvršiti sljedeći ispis:
Broj samoglasnika u stringu 'Ovo je primjer.' je 5, što čini
33,33% od ukupnog broja znakova.
'''

def samoglasnici(s):
    samoglasnici = ['a','e','i','o','u']
    broj_samoglasnika = 0
    for i in s:
        if i.lower() in samoglasnici:
            broj_samoglasnika+=1
    postotak = broj_samoglasnika/len(s)
    return postotak
pocetni_s = input("Upiši neki string : ")
d = samoglasnici(pocetni_s)
print("{:.2%}".format(d))