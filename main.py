# Enumere 5 tipos de datos en Python y suministre un valor de
# ejemplo de cada uno.

nombre = "Santiago Dulcey"
edad = 23
altura = 1.75
vacio= None
soyEstudiante = True
listaImutable = ("Hola", "pedro")
pasaTiempo = ["Programar", "Jugar", "Tocar Ukelele", 10]
listaRopa = {
    "gorra": False,
    "pantalon": "Blue" 
}
#listar el array
for tiempo in pasaTiempo:
    print(f"\t Hola soy un pasaTiempo: {tiempo}")
#Obtener la posición    
for (index,value) in enumerate(pasaTiempo):
    print(f"esta es la posición: {index}")
print(listaRopa.get("pantalon"))
print("".join(list(listaImutable)))
print(type(listaImutable))