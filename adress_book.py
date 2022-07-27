import csv
import uuid
from datetime import datetime

ID = uuid.uuid1()

Nombre = input("Ingrese su nombre: ")
Direccion = input("Ingrese su direccion: ")
Telefono = input("Ingrese su numero de telefono: ")

Fecha = datetime.today().strftime('%d-%m-%Y')

with open('Adresses.csv', 'a') as csvfile:
    fieldnames = ["ID", "Nombre", "Direccion", "Telefono", "Fecha"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    
    writer.writeheader()
    writer.writerow({"ID" : ID, "Nombre" : Nombre.upper(), "Direccion" : Direccion.upper(), "Telefono" : Telefono, "Fecha" : Fecha})

print("Datos Insertados Correctamente")    
