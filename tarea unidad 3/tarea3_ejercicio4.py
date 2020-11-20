"""Realiza un programa que pida al usuario cuantos
    números quiere introducir. Luego lee todos los números
    y realiza una media aritmética.
    """
cantidad_num = int(input("¿Cuantos numeros desea introducir ? :"))
cont = 1
sum = 0
while cont <= cantidad_num:
    num = float(input("ingresar valor " + str(cont)+" : "))
    sum += num
    cont += 1
print("promedio de los valores ingresados : {}".format(sum/cantidad_num))
