'''
1. Napišite program vjezba9_zd01.py koji od svih znakova koji se nalaze u datoteci ulaz1.txt
ispiše samo slova. Npr. za sadržaj 'Bolje 1, nego 0!' koji se nalazi u ulaznoj datoteci, program
mora ispisati 'Boljenego' '''
'''
with open('date1.txt','r') as datoteka:
    sadrzaj = datoteka.read()
'''
with open("date1.txt","r") as datoteka:
    linije = datoteka.readlines()
sadrzaj = linije[0]

for i in sadrzaj:
    if i.isalpha():
        print(i,end="")

