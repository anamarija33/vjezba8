'''
4. Napišite program vjezba11_zd04.py koji od korisnika traži unos tri točke u ravnini u vidu tri
uređena para koordinata (x_1, y_1), (x_2, y_2) i (x_3, y_3) te potom poziva funkciju
povrsina_trokuta(T_1, T_2, T_3) koja kao ulazne argumente prima tri zadana para koordinata
T_i=(x_i, y_i) i vraća površinu trokuta čiji su vrhovi T_1, T_2 i T_3. Površina se računa preko
formule:
𝑃 =
1
2
|𝑥1 ∗ (𝑦2 − 𝑦3
)+ 𝑥2 ∗ (𝑦3 −𝑦1
)+ 𝑥3 ∗ (𝑦1 − 𝑦2
)|
Ako je površina trokut jednaka 0 program treba vratiti poruku da zadane točke ne tvore
trokut, u protivnom ispisati kolika je površina zadanog trokuta.
Npr. za T_1=(-2, 4), T_2=(2, 2) i T_3=(6, 0) program ispisuje da zadane točke ne tvore trokut
jer je P=0
'''
def povrsina_trokuta(T_1,T_2,T_3):
    povrsina = (0.5*abs(T_1[0]*(T_2[1]-T_3[1])+T_2[0]*(T_3[1]-T_1[1])+T_3[0]*(T_1[1]-T_2[1])))
    if povrsina == 0:
        return "Zadane površine ne tvore trokut jer je P = 0"
    else: 
        return povrsina

koordinate = []
for i in range (3):
    coord = int(input("Upiši prvu koordinatu: "))
    coord2 = int(input("Upiši drugu koordinatu: "))
    koordinate.append((coord,coord2))
povrsina = povrsina_trokuta(koordinate[0],koordinate[1],koordinate[2])
print(povrsina)