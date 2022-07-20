def es_palindromo(palabra):
    i=0
    sigo=True
    palabra_m = palabra.lower()
    while sigo and i < ((len(palabra_m)-1)/2):
        letra1 = palabra_m[i]
        letra2 = palabra[len(palabra_m)-1-i]
        if letra1 != letra2:
            sigo = False
        i+=1    
    return sigo