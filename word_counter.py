import os

if os.path.isfile("phrases.txt"):
    with open("phrases.txt") as archivo:
        aux = archivo.readlines()
        palabras=0
        for linea in aux:
            # Agregar una sentencia if para que no sume lineas vacias
            # if linea != "":
            #     palabras=palabras+linea.count(' ') + 1
            palabras=palabras+linea.count(' ') + 1
        print(f"La cantidad de palabras existentes en el archivo es de: {palabras} y la cantidad de frases es de {len(aux)}")

print ("El programa termina cuando se ingresa la palabra fin")

frase = input(str("Escriba una frase: "))

f = open('phrases.txt', 'a')
cant_frases = 0
total_palabras=0

while (frase != 'fin'):
    total_palabras_otra_frase = frase.count(' ') + 1
    print (f"La frase tiene {total_palabras_otra_frase} palabras")
    f.write('\n' + frase )
    total_palabras = total_palabras + total_palabras_otra_frase
    cant_frases=cant_frases+1
    frase = input(str("Escriba otra frase: "))

f.close()

print(f"Usted ha ingresado un total de {total_palabras} palabras y {cant_frases} frases")
