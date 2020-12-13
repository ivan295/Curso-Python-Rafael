"""
    En este ejercicio deberás crear un script llamado personas.py que
    lea los datos de un fichero de texto, que transforme cada fila en un
    diccionario y lo añada a una lista llamada personas. Luego rocorre las personas
    de la lista y paracada una muestra de forma amigable todos sus campos.

El fichero de texto se denominará personas.txt y tendrá el siguiente contenido en
texto plano (créalo previamente):

--datos en el txt --
1;Carlos;Pérez;05/01/1989
2;Manuel;Heredia;26/12/1973
3;Rosa;Campos;12/06/1961
4;David;García;25/07/2006
    """
from io import open


def leer_fichero():
    diccionario = {}
    lista = []
    with open('personas.txt', 'r', encoding="utf8") as fichero:
        for var in fichero:
            diccio = var.split(';')
            lista.append(diccio)

    for indice, datos in enumerate(lista):
        diccionario[indice] = datos
    print("diccionario : \n", diccionario)


if __name__ == "__main__":
    leer_fichero()
