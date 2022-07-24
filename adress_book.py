import csv
from datetime import datetime

Nombre = input("Ingrese su nombre: ")
DNI = input("Ingrese su DNI: ")
Direccion = input("Ingrese su direccion: ")
Telefono = input("Ingrese su numero de telefono: ")

Fecha = datetime.today().strftime('%d-%m-%Y')

with open('Adresses.csv', 'a') as csvfile:
    fieldnames = ["ID", "Nombre", "Direccion", "Telefono", "Fecha"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    
    writer.writeheader()
    writer.writerow({"ID" : id(DNI), "Nombre" : Nombre.upper(), "Direccion" : Direccion.upper(), "Telefono" : Telefono, "Fecha" : Fecha})

print("Datos Insertados Correctamente")    
