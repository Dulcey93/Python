#12. N atletas han pasado a finales en salto triple en los juegos olímpicos de 2022. Diseñe un programa que pida por teclado los nombres de cada atleta finalista y a su vez, sus marcas del salto en metros. Informar el nombre de la atleta campeona que se quede con la medalla de oro y si rompió récord, reportar el pago que será de 500 millones. El récord esta en 15,50 metros.

# Pedimos el número de atletas finalistas
num_atletas = int(input("Ingrese el número de atletas finalistas: "))

# Inicializamos el mejor salto y el nombre del atleta campeón
mejor_salto = 0
nombre_campeon = ""

# Pedimos el nombre y la marca de salto de cada atleta
for i in range(num_atletas):
    nombre = input("Ingrese el nombre del atleta: ")
    salto = float(input("Ingrese la marca de salto en metros: "))
    
    # Si el salto es mejor que el actual mejor salto, lo actualizamos
    if salto > mejor_salto:
        mejor_salto = salto
        nombre_campeon = nombre

# Comprobamos si el atleta campeón rompió el récord
if mejor_salto > 15.50:
    print("El atleta campeón es", nombre_campeon, "y ha roto el récord. Recibirá un pago de 500 millones.")
else:
    print("El atleta campeón es", nombre_campeon, "y no ha roto el récord.")