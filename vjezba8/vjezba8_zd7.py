'''
7. Kreirajte modul moj_modul.py u koji trebate kopirati sve definicije funkcija koje ste napravili
u okviru ove vježbe. Potom lokaciju mape 'Vjezba_8' dodajte (append) u varijablu sys.path
(prethodno morate importirati modul sys). Nakon toga napišite program vjezba8_zd07.py u
kojem ćete importirati moj_modul.py i testirati neke od funkcija koje se nalaze unutar
modula moj_modul.py (testove smislite sami).
'''
import moj_modul

t = moj_modul.unos_int()
if moj_modul.prost(t):
    print("broj je prost")
else:
    print("broj je složen")