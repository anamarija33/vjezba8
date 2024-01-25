'''
6. Napišite program vjezba10_zd06.py koji crta deset koncentričnih kružnica, od kojih najveća
ima radijus duljine 300 piksela, a svaka iduća ima radijus za 10% manji od prethodne. Svaka
kružnica mora biti ispunjena jednom nijansom sive boje, pri čemu najveća kružnica mora biti
ispunjena bijelom bojom, a svaka iduća za 5% tamnijom nijansom sive boje od prethodne.
'''
from turtle import *

color = 16
radius = 300
for i in range(10):
    fillcolor(color/255,color/255,color/255)
    begin_fill()
    circle(radius,360)
    end_fill()
    t = radius*0.1
    radius = radius* 0.9
    color = color+8
    pu()
    left(90)
    fd(t)
    right(90)
    pd()