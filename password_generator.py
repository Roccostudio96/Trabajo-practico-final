
import random

mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numeros = ["1","2","3","4","5","6","7","8","9","0"]
simbolos = ["+", "-", "%", "$", "&", "#"]

op_may = input("Desea que hayan mayúsculas en la clave? S/N: ")
op_min = input("Desea que hayan minusculas en la clave? S/N: ")
op_num = input("Desea que hayan numeros en la clave? S/N: ")
op_sim = input("Desea que hayan simbolos en la clave? S/N: ")

lista_op = []
eligio_may=False
eligio_min=False
eligio_num=False
eligio_sim=False
if op_may == "S":
    lista_op = lista_op + mayusculas
    eligio_may = True
if op_min == "S":
    lista_op = lista_op + minusculas
    eligio_min = True
if op_num == "S":
    lista_op = lista_op + numeros
    eligio_num = True
if op_sim == "S":
    lista_op = lista_op + simbolos
    eligio_sim = True

try:    
    cant = int(input("Ingrese la cantidad de cifras de la contraseña (0 o caracter para generar largo por defecto): "))
except:
    cant = 16
else:
    if cant == 0:
        cant = 16


  
# Corregir el condicional, ya que siempre me devuelve una contraseña de 16 digitos
if eligio_may != True and eligio_min != True and eligio_num != True and eligio_sim != True:
    lista_op = lista_op + mayusculas + minusculas + numeros
    cant = 16

contrasenia = ''

# Se puede cambiar el rango de valores a 'range(cant)' si lo modifico 
#va a generar una contraseña de un caracter menos a lo indicado
for i in range(1,cant+1):
    contrasenia = contrasenia + random.choice(lista_op)
print(f"La contraseña quedo: {contrasenia}")
