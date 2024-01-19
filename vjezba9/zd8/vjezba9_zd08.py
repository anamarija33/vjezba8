'''
8. Napišite program vjezba9_zd08.py koji korištenjem funkcija za kompresiju teksta i
dekompresiju teksta napisanim na prošlim vježbama komprimira ili dekomprimira sadržaj
neke zadane ulazne datoteke (redak po redak), te pohranjuje dobiveni tekst u neku drugu
zadanu izlaznu datoteku. Testirajte program na način da omogućite korisniku odabir funkcije
koja će se primijeniti na unesenom tekstu (kompresija ili dekompresija) i unos naziva ulazne i
izlazne datoteke na kojoj će se primijeniti kompresija/dekompresija.
'''
'''
8. Napišite program vjezba9_zd08.py koji korištenjem funkcija za kompresiju teksta i
dekompresiju teksta napisanim na prošlim vježbama komprimira ili dekomprimira sadržaj
neke zadane ulazne datoteke (redak po redak), te pohranjuje dobiveni tekst u neku drugu
zadanu izlaznu datoteku. Testirajte program na način da omogućite korisniku odabir funkcije
koja će se primijeniti na unesenom tekstu (kompresija ili dekompresija) i unos naziva ulazne i
izlazne datoteke na kojoj će se primijeniti kompresija/dekompresija.
'''
def kompresija():
    file = open("ulaz.txt", "r")
    podaci = file.read()
    file.close()
    komprimirano = ''
    broj = 0
    slovo = podaci[0]
    for i in range(len(podaci)):
        if slovo == podaci[i]:
            broj += 1
        else : 
            komprimirano +=slovo+str(broj)
            slovo = podaci[i]
            broj = 1
        if i == len(podaci)-1:
            komprimirano+=slovo+str(broj)
    file = open("izlaz.txt","w")
    file.write(komprimirano)
    file.close()
def dekompresija():
    file = open("izlaz.txt","r")
    podaci = file.read()
    file.close()
    dekomprimirano = ''
    broj = ''
    for i in range(len(podaci)):
        if podaci[i].isalpha():
            slovo = podaci[i]
            broj =''
        if podaci[i].isnumeric():
            t = i
            while podaci[t].isnumeric():
                broj += podaci[t]
                if t<(len(podaci)-1):
                    t+=1
                else:
                    break

            i+=(t-i)
            varijabla = (slovo*int(broj))
            dekomprimirano+=varijabla
    file = open("dekompresija.txt",'w')
    file.write(dekomprimirano)
    file.close()

    
kompresija()
dekompresija()
