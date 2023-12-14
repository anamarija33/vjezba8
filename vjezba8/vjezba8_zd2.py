'''
2. Napišite program vjezba8_zd02.py koji korištenjem funkcije palindrom(s) ispituje da li je 
zadani niz znakova s palindrom (jednako se čita s lijeve i desne strane). Niz znakova treba 
unijeti korisnik, a program treba napraviti provjeru i vratiti odgovarajuću poruku.
'''
def palindrom(s):
    s2 = s[::-1]
    if s2 == s:
        print("Palindrom je. ")
    else:
        print("nije palindrom.")

s = input("upiši rič: ")
palindrom(s)