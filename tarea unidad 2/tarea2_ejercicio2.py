"""Utilizando operadores lógicos, determina si una cadena
    de texto introducida por el usuario tiene una longitud mayor
    o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False).
    """
cadena = input("ingresar cadena de texto : ")
print("¿La cadena de texto tiene una longitud mayor o igual a 3 y menor de 10? : {}" .format(
    len(cadena) >= 3 and len(cadena) < 10))
