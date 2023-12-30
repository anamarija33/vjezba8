'''
4. Napišite program vjezba9_zd04.py koji iz datoteke ulaz4.txt čita izraze oblika:
broj operacija broj
(može biti više takvih operacija u ulaznoj datoteci, ali svaka mora biti u zasebnoj liniji), te
izračunava vrijednost zadane operacije (koja može biti '+', '-', '*' ili '/') sa zadanim brojevima i
rezultat zapisuje u izlaznu datoteku izlaz4.txt (svaki rezultat u zasebnu liniju).
Npr. za sljedeći sadržaj ulazne datoteke:
4 + 11
21 * 3
program mora u izlaznu datoteku ispisati:
15
63'''
izlazna = open("izlaz4.txt",'w')

with open ("ulaz4.txt",'r') as datoteka:
    linije = datoteka.readlines()

def operacija (op, first_n, second_n):
    match op:
        case '+':
            return float(first_n) + float(second_n)
        case '-':
            return float(first_n) - float(second_n)
        case '/':
            return float(first_n) / float(second_n)
        case '*':
            return float(first_n) * float(second_n)

for i in range(0,len(linije)):
    linija = linije[i].rstrip().split(' ')
    izlazna.write(str(operacija(linija[1],linija[0],linija[2]))+'\n')

izlazna.close()
    

