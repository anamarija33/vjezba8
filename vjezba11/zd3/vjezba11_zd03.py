'''
3. Napišite program vjezba11_zd03.py koji iz ulazne datoteke ulaz.txt pročita sve izraze oblika:
Ime Prezime
(može biti više takvih izraza u ulaznoj datoteci, ali svaki mora biti u zasebnoj liniji), te ih
sortrira prema prezimenu abecednim redoslijedom i ispisuje u izlaznu datoteku izlaz.txt tako
da svako ime i prezime bude u zasebnoj liniji i da bude numerirano brojem linije.
Npr. za sljedeći sadržaj ulazne datoteke:
Marko Borko
Ivan Ivić
Stipe Antić
program mora u izlaznu datoteku ispisati:
1. Stipe Antić
2. Marko Borko
3. Ivan Ivić
'''

file = open("ulaz.txt","r")
osobe = []
for line in file:
    osobe.append(line.split())
file.close()

osobe.sort(key=lambda osobe:osobe[1])
file= open("izlaz.txt","w")
for i in range(len(osobe)):
    file.write(str(i+1)+'. '+osobe[i][0]+' '+osobe[i][1]+'\n')