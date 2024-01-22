'''
2.	Napišite program kolokvij2_zd02.py koji korištenjem funkcije upper_lower(s) ispituje koliko u zadanom nizu znakova s postoji velikih,
 a koliko malih slova engleske abecede, te koliko ostalih znakova (točaka, razmaka, znamenki i slično). Niz znakova treba unijeti korisnik,
   a glavni program potom treba pozvati funkciju upper_lower(s) sa zadanim stringom kao argumentom. Funkcija mora imati 3 povratne vrijednosti
     (broj malih slova, broj velikih slova i broj ostalih znakova), te se one ispisuju u glavnom programu (ne unutar definicije same funkcije)
       uz odgovarajuću poruku kao u donjem primjeru.
Npr. za ulazni string s='Veliko, Malo.' program može izvršiti sljedeći ispis:
U stringu ima 2 velika slova, 8 malih slova i 3 ostala znaka.
'''

def upper_lower(s):
    low = 0
    up = 0
    ostalo = 0
    for i in s:
        if i.islower():
            low+=1
        elif i.isupper():
            up+=1
        else:
            ostalo+=1
    return low,up,ostalo

s = input("Upiši neki string: ")
low,up,ostalo = upper_lower(s)
print("U stringu ima", up,"velika slova,",low,"mala slova i ",ostalo,"ostalih znakova.")