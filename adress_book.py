import csv
import uuid
from datetime import datetime

with open('Adresses.csv', 'a') as csvfile:
    
    fieldnames = ["ID", "Nombre", "Direccion", "Telefono", "Fecha"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    
    cantidad = int(input("Cuantos registros tiene para ingresar?: "))
    
    for i in range (cantidad,0,-1):
    
        ID = uuid.uuid4()
        Nombre = input("Ingrese su nombre: ")
        Direccion = input("Ingrese su direccion: ")
        Telefono = input("Ingrese su numero de telefono: ")
        Fecha = datetime.today().strftime('%d-%m-%Y')
        
        writer.writerow({"ID" : ID, "Nombre" : Nombre.upper(), "Direccion" : Direccion.upper(), "Telefono" : Telefono, "Fecha" : Fecha})

print("Datos Insertados Correctamente")    
