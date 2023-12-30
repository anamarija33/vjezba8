'''
5. Napišite program vjezba9_zd05.py koji iz ulazne datoteke ulaz5.txt (koja sadrži samo
znamenke od 0 do 9, eventualno praznine i prijelaze u novi redak) ispisuje u izlaznu datoteku
izlaz5.txt frekvencije pojavljivanja pojedine znamenke u ulaznoj datoteci (ukupan broj
pojavljivanja te znamenke podijeljen sa ukupnim brojem svih znamenaka koje se pojavljuju u
datoteci). Za prebrajanje znamenaka koristite funkciju broji_znamenke(znamenka, string)
koja vraća broj pojavljivanja zadane znamenke u zadanom stringu (funkciju trebate sami
implementirati). Npr. za skup znamenaka 0010232087 u izlaznu datoteku treba ispisati
sljedeće:
0 – 0.4
1 – 0.1
2 – 0.2
3 – 0.1
7 – 0.1
8 – 0.1'''

izlazna = open("izlaz5.txt",'w')

with open("ulaz5.txt",'r') as ulazna:
    sadrzaj = ulazna.read()
    sadrzaj = sadrzaj.replace('\n','').replace(' ','')

def broji_znamenke(znamenka,string):
    return string.count(znamenka)

for i in range(0,10):
    if str(i) in sadrzaj:
        br = broji_znamenke(str(i),sadrzaj)
        rezultat = str(i)+' - '+str(round(br/len(sadrzaj),1))
        izlazna.write(rezultat+'\n')
izlazna.close()