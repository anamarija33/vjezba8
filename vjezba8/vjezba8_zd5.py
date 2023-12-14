'''
. Napišite program vjezba8_zd05.py koji sadrži funkcije unos_int() i prost(n), te koji sadrži 
glavnu funkciju main(). Funkcija unos_int() mora od korisnika tražiti unos cijelog broja i kao 
povratnu vrijednost vraćati unos korisnika konvertiran u cjelobrojni tip (int). Funkcija prost(n)
mora imati jedan ulazni parametar n za koji mora vršiti provjeru da li je prost ili složen, te u 
ovisnosti o tome vraćati logičku vrijednost True ili False. Funkcija main() nema ulaznih 
parametara niti povratne vrijednosti, a u tijelu funkcije main() uporabom funkcija unos_int() i 
prost(n) mora se od korisnika tražiti unos cijelog broja te izvršiti provjeru je li uneseni broj 
prost ili složen i u skladu s time ispisati odgovarajuću poruku.
'''
def unos_int():
    br = int(input("Unesi cili broj : "))
    return br
def prost(n):
    br = 0
    for i in range(1,n+1):
        if n % i ==0:
            br+=1
    if br == 2:
        return True
    else: 
        return False

def main():
    t= prost(unos_int())
    if t:
        print("broj je prost")
    else:
        print("broj je složen")
main()