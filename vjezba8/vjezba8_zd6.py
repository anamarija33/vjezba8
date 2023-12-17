'''
6. Napišite program vjezba8_zd06.py koji sadrži funkcije unos_broja_u_listu(l) i max_element(l),
te koji sadrži glavnu funkciju main(). Funkcija unos_broja_u_listu(l) prima kao ulazni
parametar listu l, te mora od korisnika tražiti unos realnog broja (float) i kao povratnu
vrijednost vraćati listu l u koju je dodan broj koji je korisnik unio (ukoliko je korisnik unio
broj), a ukoliko korisnik nije unio broj onda mora vratiti neizmijenjenu listu l koja je primljena
kao ulazni parametar funkcije. Funkcija max_element(l) mora imati jedan ulazni parametar l
koji mora biti lista decimalnih brojeva, te mora vratiti maksimalni element u toj listi ako ona
nije prazna, a ako je prazna onda ne vraća ništa. Funkcija main() nema ulaznih parametara
niti povratne vrijednosti, a u tijelu funkcije main() uporabom funkcija unos_u_listu(l) i
max_element(l) mora se od korisnika tražiti unos brojeva u listu sve dok korisnik ne unese
nešto što nije broj (npr. slovo), te potom ispisati vrijednost najvećeg elementa iz unesene
liste ako ona nije prazna, u protivnom poruku da je lista prazna.
'''
def unos_broja_u_listu(l):
    broj = input("Unesi float: ")
    if broj.isdigit():
        l.append(float(broj))
        return l
    else: return l
def max_element(l):
    if len(l) != 0:
        max_elem = max(l)
        return max_elem
    else:
        return
def main():
    l = [2.3,4.5,6.5]
    l = unos_broja_u_listu(l)
    t = max_element(l)
    print(l,t)

main()
