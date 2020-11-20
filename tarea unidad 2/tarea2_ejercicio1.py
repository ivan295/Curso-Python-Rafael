"""Realiza un programa que lea 2 números por teclado y
    determine los siguientes aspectos (es suficiene con mostrar True o False):

    Si los dos números son iguales
    Si los dos números son diferentes
    Si el primero es mayor que el segundo
    Si el segundo es mayor o igual que el primero
    """
numero1 = float(input("ingresar numero 1: "))
numero2 = float(input("ingresar numero 2: "))
print("¿Son iguales ? : {}".format(numero1 == numero2))
print("¿Los numeros son diferentes ? : {}".format(numero1 != numero2))
print("¿El primer numero es mayor que el sgundo ? : {}".format(numero1 > numero2))
print("¿El segundo numero es mayor o igual que el primero ? : {}".format(
    numero2 >= numero1))
