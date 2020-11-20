"""Realiza un programa que lea dos números por teclado y permita
    elegir entre 3 opciones en un menú:

    * Mostrar una suma de los dos números
    * Mostrar una resta de los dos números (el primero menos el segundo)
    * Mostrar una multiplicación de los dos números

En caso de introducir una opción inválida, el programa informará de que no es correcta.
    """
while True:
    print("""
        **************************
        1. sumar
        2. restar
        3. multiplicar
        **************************
    """)
    opcion = int(input("elegir opcion : "))
    if opcion == 1:
        print("****** SUMA ******")
        num1 = float(input("ingresar valor 1 : "))
        num2 = float(input("ingresar valor 2 : "))
        print("el resultado de la suma es : {}".format(num1 + num2))
    if opcion == 2:
        print("****** RESTA ******")
        num1 = float(input("ingresar valor 1 : "))
        num2 = float(input("ingresar valor 2 : "))
        print(" el resultado de la resta es : {}".format(num1 - num2))
    if opcion == 3:
        print("****** MULTIPLICACION ******")
        num1 = float(input("ingresar valor 1 : "))
        num2 = float(input("ingresar valor 2 : "))
        print("el resultado de la multiplicacion es : {}".format(num1*num2))
else:
    print("finalizado...")
