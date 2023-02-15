# En la jerarquía de operadores, cuáles son los que más
# prioridad tienen cuando el intérprete de Python los evalúa?

num1, num2, num3 = 10,5,3
print("====> Respuesta N°2 <====")
print(f""" El orden de prioridad sería el siguiente para los operadores aritméticos, siendo el primero el de mayor prioridad:
    \n() Paréntesis
    \n** Exponente
    \n-x Negación
    \n* / // Multiplicación, División, Cociente, Módulo
    \n+ - Suma, Resta
    \n EJEMPLO:
    \n ({num1}*({num2}+{num3})) = {(num1*(num2+num3))} con paréntesis se realiza primero la suma 
    \n {num1}*{num2}+{num3} = {num1*num2+num3} Sin paréntesis se realiza primero la multiplicación""")