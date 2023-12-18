'''
Napišite program vjezba9_zd02.py koji u ulaznoj datoteci ulaz2.txt pronalazi sve znakove koji
se pojavljuju 2 ili više puta, te ih potom ispisuje. Ukoliko se niti jedan znak ne pojavljuje više
od jedan put onda program treba ispisati odgovarajuću poruku.
'''
with open("ulaz2.txt","r") as datoteka:
    sadrzaj = datoteka.read()

znakovi = []

for i in sadrzaj:
    if i not in znakovi and sadrzaj.count(i)>=2:
        znakovi.append(i)

print(*znakovi,sep=",")
        
