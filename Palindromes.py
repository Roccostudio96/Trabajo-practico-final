def palindromo(palabra):
    sigo = False
    for i in range(0,len(palabra)):
        if palabra[i] != palabra[len(palabra)-1-i]:
            sigo = False
        else:
            sigo = True
    return sigo

palabra = input("Ingrese una palabra para ver si es palindroma o no (bye para terminar): ")
si_palim = 0
no_palim = 0

while palabra != "bye":
    if palindromo(palabra):
        si_palim = si_palim + 1
    else:
        no_palim = no_palim + 1
    palabra = input("Ingrese una palabra para ver si es palindroma o no (bye para terminar): ")
    
print(f"La cantidad de palabras ingresada es {si_palim + no_palim} siendo la cantidad de palabras palindromes {si_palim} y la de no palindromes {no_palim}") 


