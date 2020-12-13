"""
    Realiza una función separar(lista) que tome una lista de 
    números enteros y devuelva dos listas ordenadas. La primera con 
    los números pares y la segunda con los números impares.
    """


def separar(lista):
    lista.sort()
    lista_par = []
    lista_impar = []
    for dato in lista:
        if dato % 2 == 0:
            lista_par.append(dato)
        else:
            lista_impar.append(dato)
    return lista_par, lista_impar


if __name__ == "__main__":
    user_in = input("ingresar numeros separados por comas : ")
    lista = user_in.split(',') if len(user_in) > 0 else []
    lista = [el.strip(' ') for el in lista] if len(
        user_in) > 0 else []
    lista2 = [int(num) for num in lista]
    lista_par, lista_impar = separar(lista2)
    print("pares : ", lista_par)
    print("impares : ", lista_impar)
