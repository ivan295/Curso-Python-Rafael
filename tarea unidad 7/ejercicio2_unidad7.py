"""
    Localiza el error en el siguiente bloque de código. 
    Crea una excepción para evitar que el programa se bloquee y 
    además explica en un mensaje al usuario la causa y/o solución:

    lista = [1, 2, 3, 4, 5]
    lista[10]
    """
# IndexError

lista = [1, 2, 3, 4, 5]
try:
    listshow = lista[10]
except IndexError as error:
    print("error de tipo", error.__class__)
    print("el numero ingresado esta fuera de rango del arreglo")
else:
    print(f"dato del arreglo : {listshow}")
