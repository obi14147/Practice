from random import randrange

pocet_bodu = 0
while pocet_bodu < 21:
    print('Mas ',pocet_bodu,' bodu')
    hra = input('Chces hrat? (ano/ne)')
    if hra == "ano":
        karta  = randrange(2, 11)
        print('Otocil jsi: ',karta)
        pocet_bodu = pocet_bodu + karta
    elif hra == "ne":
        break
    else:
        print('Pis ano/ne')

if pocet_bodu == 21:
    print("Vyhral jsi!")
elif pocet_bodu > 21:
    print("Presahl jsi 21")
else:
    print("Chybi ti: ",21 - pocet_bodu,"bodu.")