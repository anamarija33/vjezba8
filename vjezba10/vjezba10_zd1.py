'''
Napišite program vjezba10_zd01.py koji crta kvadrat sa stranicom duljine 400 piksela, te
njegove dijagonale. Također treba označiti vrhove kvadrata sa slovima A, B, C i D.
'''
from turtle import *
fd(200)
write("A")
goto(0,200)
write("C")
fd(200)
goto(0,0)
write("B")
left(90)
fd(200)
goto(200,0)
fd(200)
write("D")
