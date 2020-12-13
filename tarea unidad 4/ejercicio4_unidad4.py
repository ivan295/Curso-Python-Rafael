"""
    Realiza una función llamada intermedio(a, b) que a partir de dos números, devuelva 
    su punto intermedio. Cuando lo tengas comprueba el punto intermedio entre -12 y 24:

Recordatorio

El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2
    """


def intermedio(a, b):
    return (a+b)/2


if __name__ == "__main__":
    num1 = float(input("ingresar primer numero : "))
    num2 = float(input("ingresar segundo numero :"))
    inter = intermedio(num1, num2)
    print(f"el numero intermedio entre {num1} y {num2} es {inter}")
