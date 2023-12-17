import math
import sys


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

def palindrom(s):
    s2 = s[::-1]
    if s2 == s:
        print("Palindrom je. ")
    else:
        print("nije palindrom.")

def kvadrant(x,y):
    if x == 0 and y == 0:
        return 0
    elif x == 0:
        return 'y'
    elif y == 0:
        return 'x'
    elif x > 0 and y > 0:
        return '1.'
    elif x >0 and y <0:
        return '4.'
    elif x < 0 and y > 0:
        return '2.'
    else: return '3.'
    
def binarno_pretrazivanje(l,s):
    leng = len(l)
    sred = leng//2
    print(l)
    if s<l[0] or s > l[leng-1]:
        return False
    if s == l[sred]:
        print("s je jednak sred")
        return True
    elif s < l[sred]:
        print("s manji od sred")
        
        p = binarno_pretrazivanje(l[0:sred],s)
    elif s> l[sred]:
        print("s veći od sred")
        
        p =binarno_pretrazivanje(l[sred+1:leng],s)
    else:
        return False
    return p


def unos_int():
    br = int(input("Unesi cili broj : "))
    return br

def prost(n):
    br = 0
    for i in range(1,n+1):
        if n % i ==0:
            br+=1
    if br == 2:
        return True
    else: 
        return False

def unos_broja_u_listu(l):
    broj = input("Unesi float: ")
    if broj.isdigit():
        l.append(float(broj))
        return l
    else: return l


def max_element(l):
    if len(l) != 0:
        max_elem = max(l)
        return max_elem
    else:
        return


sys.path.append('Vjezba_8')