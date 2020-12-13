"""
    Realiza una función llamada agregar_una_vez(lista, el) que reciba una
     lista y un elemento. La función debe añadir el elemento al final de la lista 
     con la condición de no repetir ningún elemento. Además si este elemento ya se 
     encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar 
     y mostrar este mensaje en su lugar:

    """

elementos = [1, 5, -2]

# ValueError


def agregar_una_vez(lista, el):
    try:
        if el in elementos:
            raise ValueError
        else:
            elementos.append(el)
    except ValueError as error:
        print("error de tipo : ", error.__class__)
        print("no se pueden ingresar datos duplicados a la lista")
    else:
        print(f"lista de elementos : {elementos}")


if __name__ == "__main__":

    agregar_una_vez(elementos, el=-2)
