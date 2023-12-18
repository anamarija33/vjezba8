#čitanje cijele datoteke odjednom:
with open("ime_datoteke.txt","r") as datoteka:
    sadrzaj = datoteka.read()
    print(sadrzaj)



#čitanje datoteke liniju po liniju
with open("ime_datoteke.txt","r") as datoteka:
    linije = datoteka.readlines()
    print(linije)

#petlju za čitanja linija i obradu svake linije:
with open("ime_datoteke.txt","r") as datoteka:
    for linija in datoteka:
        print(linija)

#otvori datoteku i čitaj sadržaj
file = open("ime_datoteke.txt","r")
text = file.read()
file.close()
print(text)