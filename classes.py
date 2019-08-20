class Kotatko:
    def __init__(self, jmeno):
        self.jmeno  = jmeno

    def __str__(self):
        return 'Kotatko jmenem {}'.format(self.jmeno)

    def zamnoukej(self):
        print("{}: Mnau!".format(self.jmeno))

    def snez(self, jidlo):
        print("{}: Mnau mnau! {} mi chutna!".format(self.jmeno, jidlo))

mourek = Kotatko(jmeno = 'Mourek')
mourek.snez('ryba')
micka = Kotatko(jmeno = 'Micka')
mourek.zamnoukej()
micka.zamnoukej()
print(mourek)
print(micka)

class Kocka:
    def __init__(self):
        self.pocet_zivotu = 9

    def zamnoukej(self):
        print(" Mnau!")

    def je_ziva(self):
        return self.pocet_zivotu > 0

    def uber_zivot(self):
        if not self.je_ziva():
            print("Kocka je uz mrtva")
        else:
            self.pocet_zivotu -= 1

    def snez(self, jidlo):
        if not self.je_ziva():
            print("Je zbytecne krmit mrtvou kocku!")
            return
        if jidlo == "ryba" and self.pocet_zivotu < 9:
            self.pocet_zivotu += 1
            print("Kocka spapala rybu a obnovil se ji jeden zivot.")
        else:
            print("Kocka se krmi.")

mikes = Kocka()
mikes.zamnoukej()
mikes.snez('mys')
