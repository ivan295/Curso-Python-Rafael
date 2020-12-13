"""Realiza una función llamada recortar(numero, minimo, maximo) que 
    reciba tres parámetros. El primero es el número a recortar, el segundo es el 
    límite inferior y el tercero el límite superior. La función tendrá que cumplir 
    lo siguiente:

    Devolver el límite inferior si el número es menor que éste
    Devolver el límite superior si el número es mayor que éste.
    Devolver el número sin cambios si no se supera ningún límite.

Comprueba el resultado de recortar 15 entre los límites 0 y 10.
    """


def recortar(num, limite_i, limite_s):
    if num < limite_i:
        return limite_i
    elif num > limite_s:
        return limite_s
    else:
        return num


if __name__ == "__main__":
    num = float(input("ingresa numeero de recorte : "))
    limite_i = float(input("ingresar limite inferior : "))
    limite_s = float(input("ingresar limite superior : "))
    envio = recortar(num, limite_i, limite_s)
    print(f"devuelve : {envio}")
