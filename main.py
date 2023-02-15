# 11. Campus requiere administrar algunos datos de sus Campers
# como por ejemplo, la creación, eliminación o búsqueda de los
# developers, entre otros, por tal razón, ha solicitado el diseño de
# un programa que cuente con el siguiente menú como panel de
# control
option = 0
while(option != 2):
    option = int (input((f""" ....................MENU............................
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
    \n Digite opcion: """)))