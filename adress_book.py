# - Para el campo ID deberia ser un número aleatorio, para ello tiene una libreria integrada de python 'uuid'
import csv
from datetime import datetime

Nombre = input("Ingrese su nombre: ")
Direccion = input("Ingrese su direccion: ")
Telefono = input("Ingrese su numero de telefono: ")

Fecha = datetime.today().strftime('%d-%m-%Y')

with open('Adresses.csv', 'a') as csvfile:
    # Esta escribiendo este dato en cada ingreso, solo deberia aparecer una vez en el archivo .csv
    fieldnames = ["ID", "Nombre", "Direccion", "Telefono", "Fecha"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    
    writer.writerow({"ID" : id(Telefono), "Nombre" : Nombre.upper(), "Direccion" : Direccion.upper(), "Telefono" : Telefono, "Fecha" : Fecha})

print("Datos Insertados Correctamente")    
