# 10. En su casa le solicitan que realice un algoritmo en Python,
# que permita calcular el valor a pagar por concepto de
# energía eléctrica. Los datos que se conocen son los
# siguientes:
# - Mes de consumo - Valor kw
# -Total kw consumido en el mes - estrato

option =0
class Cuenta:
    def __init__(self, mes, valorkw, consumokw, estrato):
        self.mes = mes
        self.valorkw = valorkw
        self.consumokw =consumokw 
        self.estrato = estrato

    def calcularTotal(self):
            if(self.estrato==1):
                print(f"Valor total a pagar: {(self.consumokw * self.valorkw)*1.5}")
            elif(self.estrato==2):
                print(f"Valor total a pagar: {(self.consumokw * self.valorkw)*1.6}")
            elif(self.estrato==3):
                print(f"Valor total a pagar: {(self.consumokw * self.valorkw)*1.7}")
            elif(self.estrato==4):
                print(f"Valor total a pagar: {(self.consumokw * self.valorkw)*1.8}")
            elif(self.estrato==5):
                print(f"Valor total a pagar: {(self.consumokw * self.valorkw)*1.9}")
            elif(self.estrato==6):
                print(f"Valor total a pagar: {(self.consumokw * self.valorkw)*2.0}")

while(option != 2):
    option = int (input((f""" ====> BIENVENIDO AL MENÚ POR FAVOR ELIJA UNA OPCIÓN <====
    \n 1) Calcular valor a pagar
    \n 2) Salir
    \n""")))

    if(option==1):
        print(f""" ====> CALCULE SU VALOR A PAGAR <====""")
        mes = int (input(f"Ingresar mes de consumo *EJEMPLO: 1-2-3-4...*: "))
        valorkw = int (input(f"Ingrese el valor por kw: "))
        consumokw = int (input(f"Ingrese el número de kw consumidos en el mes: "))
        estrato = int (input(f"Ingrese su estrato: "))
        instancia = Cuenta(mes, valorkw, consumokw, estrato)
        instancia.calcularTotal()