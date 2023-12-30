'''
3. Napišite program vjezba9_zd03.py koji sve linije iz ulazne datoteke ulaz3.txt prepisuje u
izlaznu datoteku izlaz3.txt, ali tako da svaku liniju prethodno numerira.
Npr. ako je u ulaznoj datoteci zapisano:
Ovo je prva linija
Ovo je druga linija
Onda u izlaznoj datoteci nakon izvođenja programa mora pisati:
1. Ovo je prva linija
2. Ovo je druga linija'''
izlazna = open("izlaz3.txt",'w')
with open("ulaz3.txt","r") as datoteka:
    linije = datoteka.readlines()
for i in range(0,len(linije)):
    izlazna.write(str(i+1)+'. '+linije[i])

izlazna.close()