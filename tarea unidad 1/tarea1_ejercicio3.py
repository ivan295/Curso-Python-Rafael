"""El siguiente código pretende realizar una
    media entre 3 números, pero no funciona correctamente.
    ¿Eres capaz de identificar el problema y solucionarlo?
    """
numero_1 = 9
numero_2 = 3
numero_3 = 6
media = (numero_1 + numero_2 + numero_3) / 3
print("La nota media es", media)

"""el error se encuentra en la operación que se realiza en la variable media
    está devolviendo el resultado erróneo, para solucionar dicho problema
    se agregó los parentesis para asi lograr que se realice la operacion por jerarquia por
    signos de agrupación, es decir primero realizar la suma de los valores y luego dividir para
    3
 """
