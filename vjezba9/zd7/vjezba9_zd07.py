'''
7. Napišite program vjezba9_zd07.py koji u ulaznoj datoteci ulaz7.txt pronalazi sve cijele
brojeve (broj ne smije počinjati s nulom, odnosno vodeće nule treba zanemariti) te ih ispisuje
u izlaznu datoteku izlaz7.txt u uzlaznom redoslijedu (od najmanjeg) odvojene zarezom.
Npr. ako se ulaznoj datoteci nalazi sljedeći sadržaj:
Ovo su neki brojevi: 15 192 002 928.3 K005.
Onda u izlaznoj datoteci treba pisati: 2, 5, 15, 192, 928
'''
izlazna = open('izlaz7.txt','w')

with open ('ulaz7.txt','r') as ulazna:
    sadrzaj = ulazna.read()
sadrzaj = sadrzaj.split(' ')
brojevi = []
for i in sadrzaj:
    if i.islower() or i.isupper():
        w =int(''.join([zn for zn in i if zn.isnumeric()]))
        brojevi.append(w)
    else :
        if '.' in i:
            i = int(float(i))
            brojevi.append(i)
        else:
            brojevi.append(int(i))
brojevi.sort()
brojevi= (', '.join(str(i) for i in brojevi))
izlazna.write(brojevi)
izlazna.close()