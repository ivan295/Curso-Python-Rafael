"""
Localiza el error en el siguiente bloque de código. 
Crea una excepción para evitar que el programa se bloquee y 
además explica en un mensaje al usuario la causa y/o solución:

resultado = 15 + "20"
"""
# TypeError:
try:
    resultado = 15 + "20"
except TypeError as error:
    print("error de tipo : ", error.__class__)
    print("no se pudo realizar la operacion ya que existen tipos de datos no soportados")
else:
    print(f"el resultado de la operacion es : {resultado}")
