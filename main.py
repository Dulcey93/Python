# Escriba un bloque cualquiera de código en Python en donde
# utilice 2 condicionales (if) anidados.

num1,num2,num3= 1,2,3

if(num1<=num2):
    if(num2<=num3):
        print(f"{num3} es el mayor")
    else: 
        print(f"{num2} es mayor que {num3}")
else:
    print(f"{num1} es mayor que {num2}")