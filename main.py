# Construya un algoritmo en Python, que permita ingresar la
# información de un empleado e imprima el nombre, los
# apellidos y la antigüedad. Los datos que se deben solicitar
# son los siguientes:
# *Nombre * Teléfono *Año de ingreso a la empresa
# *Apellidos *Edad.
import datetime
option =0
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = int(date.strftime("%Y"))
class Person:
    def __init__(self, nombre, apellido, edad, telefono, fecha_ingreso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.fecha_ingreso = fecha_ingreso

    def imprimir(self):
        antiguedad = year - int(self.fecha_ingreso)
        return print(f"***===============> El empleado {self.nombre} {self.apellido} tiene {antiguedad} años en la empresa ///********** \t \n")

while(option != 3):
    option = int (input((f""" ====> MENÚ EMPLEADOS <====
    \n 1) Ingresar empleado
    \n 2) Imprimir empleado
    \n 3) Salir
    \n""")))

    if(option==1):
        print(f""" ====> INGRESAR EMPLEADO <====""")
        nombre = input(f"Ingrese el nombre: ")
        apellido = input(f"Ingrese el apellido: ")
        edad = input(f"Ingrese la edad: ")
        telefono = input(f"Ingrese el telefono: ")
        fecha_ingreso = input(f"Ingrese la fecha de ingreso *EJEMPLO 2017*: ")
        instancia = Person(nombre, apellido, edad, telefono, fecha_ingreso)
    if(option==2):
        instancia.imprimir()