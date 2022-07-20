print ("El programa termina cuando se ingresa la palabra fin")

frase = input(str("Escriba una frase: "))
total_palabras = frase.count(' ') + 1
print (f"La frase tiene {total_palabras} palabras")

f = open('phrases.txt', 'a')
f.write('\n' + frase )

while (frase != 'fin'):
    frase = input(str("Escriba otra frase: "))
    total_palabras_otra_frase = frase.count(' ') + 1
    print (f"La frase tiene {total_palabras_otra_frase} palabras")
    f.write('\n' + frase )
    total_palabras = total_palabras + total_palabras_otra_frase

f.close()

total_palabras = total_palabras - 1
file = open ('phrases.txt')
print(file.read())
print(f"Usted ha ingresado un total de {total_palabras} palabras")
