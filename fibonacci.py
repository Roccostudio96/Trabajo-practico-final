
def suma(a, b):
    return (a + b)

nro = int(input('Ingrese un numero entero mayor que 0: '))
while nro <= 0:
    print(f"El numero ingresado no es mayor que 0, intente nuevamente: ")
    nro = int(input('Ingrese un numero entero mayor que 0: '))

if nro != 1:
    nro1 = 1
    nro2 = 1
    contador = nro - 2
    fibo = [nro1,nro2]

    while contador > 0:
        nro3 = suma(nro1,nro2)
        fibo.append(nro3)
        nro1=nro2
        nro2=nro3
        contador=contador-1
else:
    fibo = [1]
    
print(f'La sucesión de fibonacci del numero {nro} es: {fibo}')
