'''
6. Napišite program vjezba9_zd06.py koji iz ulazne datoteke ulaz6.txt u kojoj se u svakom
zasebnom retku nalazi ime osobe, njegova težina (u kg) i njegova visina (u metrima) u izlaznu
datoteku izlaz6.txt ispisuje sva imena osoba zajedno sa njihovim indeksom tjelesne mase
(indeks tjelesne mase se izračunava kao kvocijent mase i kvadrata visine osobe), s tim da
osobe u izlaznoj datoteci moraju biti sortirane silazno prema indeksu tjelesne mase.
Npr. ako je u ulaznoj datoteci zapisano:
Ivan 68 1.73
Marko 91 1.85
Onda u izlaznoj datoteci nakon izvođenja programa mora pisati:
Marko 26.59
Ivan 22.72
'''
izlazna = open('izlaz6.txt', 'w')
izlaz_osobe = []
with open ('ulaz6.txt','r') as ulazna:
    osobe = ulazna.readlines()
for i in range(0, len(osobe)):
    red = osobe[i].rstrip().split(' ')
    rezultat = red[0]+ ' '+str(round(float(red[1])/pow(float(red[2]),2),2))
    izlaz_osobe.append(rezultat)
def funct(e):
    return e[-5:]
izlaz_osobe.sort(reverse = True,key = funct)
for i in izlaz_osobe:
    izlazna.write(i+'\n')
'''
profesorovo rjšenje
niz = []
niz2=[]
file = open("ulaz6.txt","r")
for line in file:
    niz.append(line.split())
file.close()
for i in range(len(niz)):
    x =float(niz[i][1])/(float(niz[i][2])**2)
    niz2.append((niz[i][0],str(x)))

niz2.sort(key=lambda niz2:niz2[1],reverse = True)
file = open("izlaz6.txt",'w')
for i in range(len(niz2)):
    file.write(niz2[i][0]+' '+niz2[i][1]+"\n")
file.close()
print(niz2)
'''
