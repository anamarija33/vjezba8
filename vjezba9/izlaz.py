#Upisivanje u tekstualnu datoteku s with blokom: 
with open('izlazna_datoteka.txt','w') as datoteka:
    datoteka.write("ovo je primjer teksta koji zapappapap")

#upisivanje u textualnu datoteku bez bloka:
datoteka = open('izlazna_datoteka.txt','w')
datoteka.write("ovo jep rimejr teksta babsdkjlads")
datoteka.close()