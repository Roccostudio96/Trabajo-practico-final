# realizar conteo de palabras de una frase ingresada por el usuario.
# ademas debe registrar las frases ingresadas en u archivo de teto
# cada ve que se ejecuta el algoritmo debe mostrar un resumen de frases ingresadas y total de palabras


def cuento_palabras(frase):
    nro = 0
    for i in range(0,len(frase)-1):
        if frase[i] == " ":
            nro += 1
    if nro != 0 or frase != "":
        nro += 1
    return nro

def imprimir_cuento_archivo():
    with open("phrases.txt","r") as archivo_leido:
        aux = archivo_leido.readlines()
        auxiliar_palabra = 0
        for linea in aux:
            print(linea)
            auxiliar_palabra = auxiliar_palabra + cuento_palabras(linea)
    return auxiliar_palabra


import os

# comprobar si el archivo phrases.txt existe o no
if os.path.isfile("phrases.txt"):
    #si existe pasar por pantalla lo que hay, y tomar de la primer linea las palabras ingresadas
    with open("phrases.txt","r") as arch_lee:
        archivo_leido = arch_lee.readlines()
        nro_palabras = imprimir_cuento_archivo()
        print(f"Palabras existentes en el archivo: {nro_palabras} y frases: {len(archivo_leido)}")
else:
    nro_palabras = 0

cont_inicial = nro_palabras
    
with open("phrases.txt","a") as archivo:

    frase = input("Ingrese una frase ('finaliza aca' o 'show time' para terminar): ")

    while frase != "finaliza aca" and frase != "show time":
        palabras = cuento_palabras(frase)
        print(f"La cantidad de palabras ingresadas fue de {palabras}")
        archivo.write(frase + "\n")
        nro_palabras = nro_palabras + palabras
        frase = input("Ingrese una frase ('finaliza aca' o 'show time' para terminar): ")


print(f"la cantidad de palabras ingresadas más las que había en el archivo fueron {nro_palabras}")
print(f"El archivo quedó: ")
imprimir_cuento_archivo()  

    
    