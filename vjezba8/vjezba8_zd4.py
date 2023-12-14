'''
4. Napišite program vjezba8_zd04.py koji korištenjem rekurzivne funkcije 
binarno_pretrazivanje(l,s) traži element s u sortiranoj listi brojeva l. Binarno pretraživanje 
niza (binary search) traži element u sortiranoj listi na način da ga uspoređuje sa srednjim 
elementom u listi i ako je srednji element veći od zadanog onda se uzima lijeva polovica liste i 
ponavlja se poziv funkcije na toj polovici, a u protivnom se uzima desna polovica liste. 
Postupak se ponavlja rekurzivno sve dok se ne pronađe zadani element u listi, ili dok se ne 
iscrpi lista. Funkcija vraća True ili False u ovisnosti o tome je li zadani element pronađen ili 
nije'''
def binarno_pretrazivanje(l,s):
    leng = len(l)
    sred = leng//2
    print(l)
    if s<l[0] or s > l[leng-1]:
        return False
    if s == l[sred]:
        print("s je jednak l")
        return True
    elif s < l[sred]:
        print("s manji od l")
        
        p = binarno_pretrazivanje(l[0:sred],s)
    elif s> l[sred]:
        print("s veći od l")
        
        p =binarno_pretrazivanje(l[sred+1:leng],s)
    else:
        return False
    return p
# unit if ako je s>len(l)
s = 200
l = list(range(100))
print(l)
t=binarno_pretrazivanje(l,s)
if t:
    print("Broj je pronađen")
else:
    print("Broj nije pronađen")