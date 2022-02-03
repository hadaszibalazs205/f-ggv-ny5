'''
5. Feladat
Írj egy programot, ami addig kér be egész pozitív számokat, amíg a felhasználó negtív számot nem ír! 
A megadott számokat tárolja a program egy listában, és ezt adja át paraméterként egy függvények, amely a lista legkisebb elemével tér vissza. 
A program írja ki, hogy melyik volt a megadott legkisebb szám!
'''

lista = []
while True:
    szam = int(input("Kérek egy számot: "))
    if szam > 0:
        lista.append(szam)
    else:
        break
def legkisebb(lista):
    return min(lista)

print(legkisebb(lista))