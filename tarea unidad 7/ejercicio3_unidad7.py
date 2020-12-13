"""
    Localiza el error en el siguiente bloque de código. 
    Crea una excepción para evitar que el programa se bloquee y 
    además explica en un mensaje al usuario la causa y/o solución:

    colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
    colores['blanco']
    """
# KeyError:
colores = {'rojo': 'red', 'verde': 'green', 'negro': 'black'}
try:
    diccshow = colores['blanco']
except KeyError as error:
    print("error de tipo : ", error.__class__)
    print("no existe esta clave en el diccionario")
else:
    print(f"dato extraido con la clave ingresada : {diccshow}")
