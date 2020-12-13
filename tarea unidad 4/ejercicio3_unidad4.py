"""
    Realiza una función llamada relacion(a, b) que a partir de dos números 
    cumpla lo siguiente:

    Si el primer número es mayor que el segundo, debe devolver 1.
    Si el primer número es menor que el segundo, debe devolver -1.
    Si ambos números son iguales, debe devolver un 0.

Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'.
    """


def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    elif a == b:
        return 0


if __name__ == "__main__":
    num1 = float(input("ingresar numero 1 : "))
    num2 = float(input("ingresar numero 2 : "))
    respuesta = relacion(num1, num2)
    print(f"respuesta = {respuesta}")
