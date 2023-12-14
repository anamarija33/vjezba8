'''
1. Napišite program vjezba8_zd01.py koji sadrži definicije sljedećih funkcija:
a) Funkcija zbroj koja zbraja dva prirodna broja koji su ulazni parametri funkcije i vraća 
vrijednost zbroja.
b) Funkcija zbroj_znamenaka koja kao ulazni parametar prima cijeli broj i vraća zbroj 
njegovih znamenaka.
c) Funkcija udaljenost_od_0 koja kao ulazni parametar prima dva realna broj koji 
predstavljaju x i y koordinatu neke točke u koordinatnom sustavu, te vraća 
udaljenost te točke od ishodišta koordinatnog sustava (formula 𝑑 = √𝑥
2 + 𝑦
2).
d) Funkcija udaljenost_tocaka koja za dva uređena para (x_1, y_1) i (x_2, y_2) računa i 
vraća udaljenost između točaka T_1 i T_2 zadanih pomoću ovih parova koordinata 
a u 
koordinatnom sustavu (formula 𝑑(𝑇_1, 𝑇_2) = √(𝑥_1−𝑥_2)
2 + (𝑦_1 − 𝑦_2)
2).'''
import math
def zbroj(broj1, broj2):
    zbr = broj1 + broj2
    return zbr

def zbroj_znamenaka(broj):
    s_br = str(broj)
    zbroj = 0
    for i in s_br:
        zbroj+=int(i)
    return zbroj
def udaljenost_od_0(x, y):
    d = math.sqrt(x**2+y**2)
    return round(d,2)
def udaljenost_tocaka(x1,y1,x2,y2):
        d=math.sqrt((x1-x2)**2+(y1-y2)**2)
        return round(d,2)

a = int(input("unesi broj: "))
b = int(input("uensi drugi broj: "))
print("zbroj: ",zbroj(a,b))
print("zbroj zn:",zbroj_znamenaka(a))

a = float(input("unesi realni br: "))
b = float(input("uensi realni broj: "))
print("udaljenost od ishodišta: ", udaljenost_od_0(a,b))

x1= int(input("Unesi x koordinatu: "))
y1 = int(input("Unesi y koordinatu: "))
x2= int(input("Unesi x koordinatu: "))
y2 = int(input("Unesi y koordinatu: "))

print(udaljenost_tocaka(x1,y1,x2,y2))
