#13. En pocos días comienza la vuelta a España y la federación colombiana de ciclismo, como incentivo ha determinado pagar un valor adicional. Cree un programa en Python que pida por teclado el sueldo básico por kilometro recorrido, el número de kilómetros recorridos durante toda la vuelta, numero de kilómetros recorridos con la camiseta de líder. Calcular el valor a pagar total, si se sabe que si recorre en la bici más de 1800 kilómetros con la camiseta de líder, esos kilómetros se consideran especiales y tendrán un recargo de 25%. El total de kilómetros por recorrer durante toda la vuelta serán 3.277 kilómetros,el ganador de la vuelta a España recibirá 700 millones de pesos colombianos.

# Pedimos el sueldo básico por kilómetro recorrido, los kilómetros totales y los kilómetros con la camiseta de líder
sueldo_km = float(input("Ingrese el sueldo básico por kilómetro recorrido: "))
km_totales = int(input("Ingrese el número de kilómetros recorridos durante toda la vuelta: "))
km_lider = int(input("Ingrese el número de kilómetros recorridos con la camiseta de líder: "))

# Calculamos el valor a pagar sin el recargo por los kilómetros especiales
valor_sin_recargo = sueldo_km * km_totales

# Si los kilómetros con la camiseta de líder son más de 1800, aplicamos el recargo del 25%
if km_lider > 1800:
    km_recargo = km_lider - 1800
    valor_recargo = sueldo_km * km_recargo * 0.25
    valor_total = valor_sin_recargo + valor_recargo
else:
    valor_total = valor_sin_recargo

# Informamos el valor total a pagar
print("El valor total a pagar es:", valor_total, "pesos colombianos.")

# Comprobamos si el ciclista es el ganador de la vuelta a España
if km_lider == km_totales:
    print("¡Felicitaciones! Eres el ganador de la vuelta a España y recibirás un premio de 700 millones de pesos colombianos.")
