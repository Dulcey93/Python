
# 11. Campus requiere administrar algunos datos de sus Campers
# como por ejemplo, la creación, eliminación o búsqueda de los
# developers, entre otros, por tal razón, ha solicitado el diseño de
# un programa que cuente con el siguiente menú como panel de
# control
class Grupo:
    def __init__(self, team, nombreteam):
        self.team = team
        self.nombreteam = nombreteam

    def Crear(self):
            print(f"Se creó el grupo exitosamente {self.nombreteam} --> En estos momentos está vacío")

    def Listar(self):
            print(f"--> Estos son los nombres de los estudiantes en {self.nombreteam}")
            for estudiante in self.team:
                print(f"{estudiante}")

    def Agregar(self, nombrecamper):
            self.team.append(nombrecamper)

    def Eliminar(self, nombrecamper):
            self.team.remove(nombrecamper)
    
    def Ordenar(self):
            print(f"Lista desordenada del team {self.nombreteam}")
            for estudiante in self.team:
                print(f"{estudiante}")
            self.team.sort()
            print(f"Lista ordenada del team {self.nombreteam}")
            for estudiante in self.team:
                print(f"{estudiante}")
    
    def Buscar(self,nombrecamper):
            if(nombrecamper in self.team):
                indice = self.team.index(nombrecamper)
                print(f"El camper {nombrecamper} está en el grupo {self.nombreteam} en la posición: {indice}")

option = 0
validation = False
while(option != 3):
    option = float (input((f""" ....................................................MENU...............................................................
    \n 1.  CREAR GRUPO ARTEMIS:
    \n 1.1 LISTAR CAMPERS DE ARTEMIS
    \n 1.2 AGREGAR CAMPERS A ARTEMIS
    \n 1.3 ELIMINAR CAMPERS DE ARTEMIS
    \n 1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS
    \n 1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS
    \n 2.  CREAR GRUPO SPUTNIK:
    \n 2.1 LISTAR CAMPERS DE SPUTNIK:
    \n 2.2 AGREGAR CAMPERS A SPUTNIK
    \n 2.3 ELIMINAR CAMPERS DE SPUTNIK
    \n 2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK
    \n 2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK
    \n 3.  SALIR
    \n Digite opcion: """)))
    if option == 1:
        print("====CREAR TEAM====")
        artemis=[]
        validation = True
        artemisobj = Grupo(artemis, nombreteam="Artemis")
        artemisobj.Crear()
    if(validation):
        if option == 1.1:
            print("====LISTAR CAMPERS====")
            artemisobj.Listar()
        if option == 1.2:
            print("====AGREGAR CAMPER====")
            nombrecamper = input("Ingrese el nombre del camper: ")
            artemisobj.Agregar(nombrecamper)
            print(f"El estudiante '{nombrecamper}' se agregó al grupo: {artemisobj.nombreteam}")
        if option == 1.3:
            print("====ELIMINAR CAMPER====")
            nombrecamper = input("Ingrese el nombre del camper: ")
            artemisobj.Eliminar(nombrecamper)
            print(f"El estudiante '{nombrecamper}' se eliminó del grupo: {artemisobj.nombreteam}")
        if option == 1.4:
            print("====ORDENAR TEAM ALFABETICAMENTE====")
            artemisobj.Ordenar()
        if option == 1.5:
            print("====BUSCAR CAMPER====")
            nombrecamper = input("Ingrese el nombre del camper: ")
            artemisobj.Buscar(nombrecamper)
    else:
        print(f"El grupo está vacío por favor ingrese estudiantes")
    
        if option == 2:
            print("====CREAR TEAM====")
            sputnik=[]
            validation = True
            sputnikobj = Grupo(sputnik, nombreteam="Sputnik")
            sputnikobj.Crear()
        if(validation):
            if option == 2.1:
                print("====LISTAR CAMPERS====")
                sputnikobj.Listar()
            if option == 2.2:
                print("====AGREGAR CAMPER====")
                nombrecamper = input("Ingrese el nombre del camper: ")
                sputnikobj.Agregar(nombrecamper)
                print(f"El estudiante '{nombrecamper}' se agregó al grupo: {sputnikobj.nombreteam}")
            if option == 2.3:
                print("====ELIMINAR CAMPER====")
                nombrecamper = input("Ingrese el nombre del camper: ")
                sputnikobj.Eliminar(nombrecamper)
                print(f"El estudiante '{nombrecamper}' se eliminó del grupo: {sputnikobj.nombreteam}")
            if option == 2.4:
                print("====ORDENAR TEAM ALFABETICAMENTE====")
                sputnikobj.Ordenar()
            if option == 2.5:
                print("====BUSCAR CAMPER====")
                nombrecamper = input("Ingrese el nombre del camper: ")
                sputnikobj.Buscar(nombrecamper)
                print(f"El estudiante '{nombrecamper}' se eliminó del grupo: {sputnikobj.nombreteam}")
        else:
            print(f"El grupo está vacío por favor ingrese estudiantes")
