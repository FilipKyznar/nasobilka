import random

def nasobeni(a, b):

    vysledek = a * b

    return vysledek

body= 0

def kontrola(vysledek, vysledek_zak):

    global body

    if vysledek == vysledek_zak:

        print("Máš to správně")
        print(body)
        body=body+1
        
        
        

    else:

        print("Máš to špatně")

    return body    

for nasobilka in range(9):

    a = random.randint(1, 10)
    b = random.randint(1, 10)

    vysledek_zak = int(input (f"{a} * {b} = "))
    
    vysledek = nasobeni(a,b)

    kontrola(vysledek,vysledek_zak)

print ("Celkový počet bodů je",body)
