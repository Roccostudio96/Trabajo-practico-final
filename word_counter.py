# - Una forma de mejorar el codigo es reducir los inputs con alguna variable auxiliar
# - Hay que corregir el contador de frases cuando el archivo ya posee frases almacenadas, ya que devuelve un valor de más
import os

with open("phrases.txt") as archivo:
    aux = archivo.readlines() 
    palabras=0
    for linea in aux:
        palabras=palabras+linea.count(' ') + 1
    print(f"La cantidad de palabras existentes en el archivo es de: {palabras} y la cantidad de frases es de {len(aux)}")

print ("El programa termina cuando se ingresa la palabra fin")

frase = input(str("Escriba una frase: "))
total_palabras = frase.count(' ') + 1
#total_frases = 0
 
#print (f"La frase tiene {total_palabras} palabras")

f = open('phrases.txt', 'a')
#f.write('\n' + frase )

while (frase != "fin"):
    #frase = input(str("Escriba otra frase: "))
    #total_frases = total_frases + 1
    total_palabras_otra_frase = frase.count(' ') + 1
    print (f"La frase tiene {total_palabras_otra_frase} palabras")
    f.write('\n' + frase )
    total_palabras = total_palabras + total_palabras_otra_frase
    frase = input(str("Escriba otra frase: "))

f.close()

total_palabras = total_palabras - 1
file = open ('phrases.txt')
#print(file.read())
print(f"Usted ha ingresado un total de {total_palabras} palabras ")

file.close()    
