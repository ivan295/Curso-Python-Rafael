"""
    Realiza una función llamada area_circulo(radio) que devuelva el 
    área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio:

Recordatorio

El área de un círculo se obtiene al elevar el radio a dos y multiplicando 
el resultado por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del 
módulo math:

Código
Resultado
78.53981633974483
    """
import math


def area_circulo(radio):
    return (math.pi*(radio**2))


if __name__ == "__main__":
    radio = 5
    area = area_circulo(radio)
    print(f"el circulo con radio : {radio} tiene un area de : {area}")
