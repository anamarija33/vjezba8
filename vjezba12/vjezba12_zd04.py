'''
4.	Napišite program kolokvij2_zd04.py koji od korisnika traži unos jedne točke u ravnini u vidu uređenog para koordinata (x, y)
 te potom poziva funkciju projekcija_na_os _x(T) koja kao ulazni argument prima zadanu točku T=(x, y) i vraća točku Tx=(x, 0). 
 U glavnom programu korisnik unosi koordinate točke T=(x, y) nakon čega se poziva funkcija projekcija_na_os_x(T). Povratna vrijednost 
 funkcije također se ispisuje u glavnom programu (ne unutar definicije funkcije).
Npr. za T=(-1, 5) program ispisuje da je njena projekcija na os x točka Tx=(-1, 0).
'''

x = int(input("Upiši x koordinatu: "))
y = int(input("Upiši y koordinatu: "))
T = (x,y)
def projekcija_na_os_x(T):
    return (T[0],0)

Tocka = projekcija_na_os_x(T)
print("Za",T,"program ispisuje da je njena projekcija na os x točka Tx = ",Tocka)