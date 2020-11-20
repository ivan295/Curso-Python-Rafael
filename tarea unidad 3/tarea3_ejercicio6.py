"""
    Utilizando la función range() y la conversión a listas genera las siguientes
    listas dinámicamente:

    Todos los números del 0 al 10 [0, 1, 2, ..., 10]
    Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
    Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
    Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
    Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

Concepto útil

Se pueden generar saltos en el range() estableciendo su tercer parámetro range(inicio, fin, salto),
experimenta.
    """
print("lista del 0 al 10 : {}".format(list(range(0, 11))))
print("lista del -10 al 0 : {}".format(list(range(-10, 1))))
print("lista de pares de 0 al 20 : {}".format(list(range(0, 21, 2))))
print("lista de impares entre -20 y 0 : {}".format(list(range(-19, 1, 3))))
print("lista de los multiplos de 5 del 0 al 50 : {}".format(list(range(5, 51, 5))))
