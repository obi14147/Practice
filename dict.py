a = {'jmeno': 'Anna', 'mesto': 'Brno', 'cisla': [3, 7]}
print(a['jmeno'])
a['cisla'] = [5, 8, 7] #zmena hodnoty podle klice
print(a)
a['jazyk'] = 'Python' #Pridani hodnoty
print(a)
del a['cisla']
print(a)

#lookup table
cisla = {'Maruška': '153 85283', 'Terka': '237 26505', 'Renata': '385 11223', 'Michal': '491 88047'}
barvy = {'hruška': 'zelená', 'jablko': 'červená', 'meloun': 'zelená', 'švestka': 'modrá', 'ředkvička': 'červená',
    'zelí': 'zelená', 'mrkev': 'červená'}

#slovnik v cyklu for vyhodi klice
popisy_funkci = {'len': 'délka', 'str': 'řetězec', 'dict': 'slovník'}
for klic in popisy_funkci:
    print(klic)
#Pro hodnoty je potreba popuzit fci values
for hodnota in popisy_funkci.values():
    print(hodnota)
#Pro keys i values je potreba fce items
for klic, hodnota in popisy_funkci.items():
    print('{}: {}'.format(klic, hodnota))

#Vytvoreni slovniku pomoci fce dict
barvy_po_tydnu = dict(barvy)
for klic in barvy_po_tydnu:
    barvy_po_tydnu[klic] = 'černo-hnědo-' + barvy_po_tydnu[klic]
print(barvy['jablko'])
print(barvy_po_tydnu['jablko'])

data = [(1, 'jedna'), (2, 'dva'), (3, 'tri')]
nazvy_cisel = dict(data)
print(nazvy_cisel)

popisy_funkci = dict(len='delka', str='retezec', dict='slovnik')
print(popisy_funkci['len'])