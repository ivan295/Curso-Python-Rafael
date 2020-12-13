"""A partir del ejercicio anterior, vamos a suponer que cada número es una nota, y lo 
    que queremos es obtener la nota final. El problema es que cada nota tiene un valor porcentual:

    La primera nota vale un 15% del total
    La segunda nota vale un 35% del total
    La tercera nota vale un 50% del total

Desarrolla un programa para calcular perfectamente la nota final:

nota_1 = 10
nota_2 = 7
nota_3 = 4
    """
nota_1 = 10
nota_2 = 7
nota_3 = 4
print("suma total: {}".format(round((10*0.15)+(7*0.35)+(4*0.5))))
print("el promedio es : {}".format(round(((10*0.15)+(7*0.35)+(4*0.5)) / 3)))
