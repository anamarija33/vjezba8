'''
3. Napišite program vjezba8_zd03.py koji od korisnika traži unos dva broja x i y te pomoću 
funkcije kvadrant(x,y) provjerava i vraća redni broj kvadranta u kojem se nalazi točka (x, y).
Ukoliko se točka nalazi na nekoj od koordinatnih osi program treba vratiti naziv osi na kojoj 
se nalazi zadana točka (npr. x), a u koliko se točka nalazi u ishodištu onda treba vratiti 0.
'''
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

prvi = int(input("upiši x : "))
drugi = int(input("Upiši y : "))
print(kvadrant(prvi,drugi))