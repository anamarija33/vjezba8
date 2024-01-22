'''
3.	Napišite program kolokvij2_zd03.py koji iz ulazne datoteke kalorije.txt čita izraze oblika:
Naziv_jela Broj_kalorija
(može biti više takvih izraza u ulaznoj datoteci, ali svaki mora biti u zasebnoj liniji), te ih sortira silazno (od veće prema manjoj) prema veličini i ispisuje
 u izlaznu datoteku sortirano.txt tako da svaki zapis bude u zasebnoj liniji. Pri tome pretpostavljamo da naziv jela ne smije sadržavati razmake, te da je broj
   kalorija cijeli broj.
Npr. za sljedeći sadržaj ulazne datoteke:
Pizza 1100
Sarma 950
Janjetina 1500
program mora u izlaznu datoteku ispisati:
Janjetina 1500
Pizza 1100
Sarma 950
'''
lista = []
linija = ''
file = open("kalorije.txt",'r')
for i in file:
    i=i.strip().split()
   # t = [i[0],int(i[1])]
    lista.append(i)
lista.sort(key= lambda lista:int(lista[1]),reverse = True)
file.close()
file = open("sortirano.txt","w")
for i in lista:
    #t = i[0]+' '+str(i[1])+'\n'
    file.writelines(' '.join(i)+'\n')
