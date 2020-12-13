"""
    Localiza el error en el siguiente bloque de código. 
    Crea una excepción para evitar que el programa se bloquee y además 
    explica en un mensaje al usuario la causa y/o solución:

    resultado = 10/0
    """
# error ZeroDivisionError
try:
    resultado = 10/0
except ZeroDivisionError as error:
    print("error de tipo : ", error.__class__)
    print("no se puede dividir para 0")
else:
    print(f"la division se realizó con exito : {resultado}")
