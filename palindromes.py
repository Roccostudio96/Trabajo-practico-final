import palindromo

palabra = input("Ingrese una palabra para ver si es palindrome o no (bye para terminar): ")
si_palim = 0
no_palim = 0

while palabra != "bye":
    if palindromo.es_palindromo(palabra):
        si_palim += 1
        print(f"La palabra {palabra} es palindrome")
    else:
        no_palim += 1
        print(f"La palabra {palabra} no es palindrome")
    palabra = input("Ingrese una palabra para ver si es palindrome o no (bye para terminar): ")

print(f"La cantidad de palabras ingresadas es {si_palim + no_palim} siendo la cantidad de palabras palindromes {si_palim} y la de no palindromes {no_palim}") 
