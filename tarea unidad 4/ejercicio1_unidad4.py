"""
    Realiza una función llamada area_rectangulo(base, altura) que devuelva el área del 
    rectangulo a partir de una base y una altura. Calcula el área de un rectángulo
     de 15 de base y 10 de altura:

Recordatorio

El área de un rectángulo se obtiene al multiplicar la base por la altura.
    """


def area_rectangulo(base, altura):
    return base*altura


if __name__ == "__main__":
    base = 15
    altura = 10
    area = area_rectangulo(base, altura)
    print(
        f"triangulo con base : {base} y altura : {altura} tiene un area de : {area}")
