# - Una forma de mejorar el codigo es reducir los inputs con alguna variable auxiliar
# - Hay que corregir el contador de frases cuando el archivo ya posee frases almacenadas, ya que devuelve un valor de más
import os

with open("phrases.txt") as archivo:
    aux = archivo.readlines() 
    palabras= 0
    for linea in aux:
        palabras=palabras+linea.count(' ') + 1

archivo = open("phrases.txt", "rt")
datos = archivo.read()
palabras = datos.split()

print(f"La cantidad de frases que tiene el archivo es de {len(aux)}")
print(f"La cantidad total de palabras que tiene el archivoes de {len(palabras)}")

archivo.close()

print("El programa termina cuando se ingresa la palabra fin")

f = open('phrases.txt', 'a')

frase = input(str("Escriba una frase: "))
 
while (frase != "fin"):
    f.write('\n' + frase)
    total_palabras = frase.count(' ') + 1
    frase = input(str("Escriba otra frase: "))
    total_palabras_otra_frase = frase.count(' ') + 1
    total_palabras = total_palabras + total_palabras_otra_frase

f.close()

with open("phrases.txt") as archivo:
    aux = archivo.readlines() 
    palabras= 0
    for linea in aux:
        palabras=palabras+linea.count(' ') + 1

archivo = open("phrases.txt", "rt")
datos = archivo.read()
palabras = datos.split()

print(f"Ahora hay {len(aux)} frases y {len(palabras)} palabras")

archivo.close()
