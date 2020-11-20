"""Dadas dos listas, debes generar una tercera con
    todos los elementos que se repitan en ellas, pero no debe
    repetirse ningún elemento en la nueva lista:
    """
lista1 = ['h', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
lista2 = ['h', 'o', 'l', 'a', ' ', 'l', 'u', 'n', 'a', 'm', 'h']
lista3 = []
for x in lista1:
    if x in lista2 and x not in lista3:
        lista3.append(x)
print(lista3)
