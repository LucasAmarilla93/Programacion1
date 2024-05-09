import random
from Package_arrays.Input import * 
from Package_arrays.Validate import * 
from Package_arrays.Metodos_matrices import * 
from os import system
"""
Práctica de Matrices
Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total tiene 15 choferes (cada uno con un legajo distinto generado aleatoriamente).
Nos piden desarrollar un software que presente el siguiente menú  de usuarios:
Menú:
Cargar planilla. El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos). Si el chofer existe cargará la recaudación del viaje indicando línea y coche (no necesariamente un chofer está asignado a una única línea y coche), estos datos deben estar validados. Un chofer puede cargar más de una recaudación por día (para distintas líneas y distintos coches). Cada coche de cada línea puede tener varias recaudaciones diarias.
Mostrar la recaudación de todos los coches y líneas.
Calcular y mostrar recaudación por línea.
Calcular y mostrar recaudación por coche. / CADA UNO DE LOS 15 COCHES. 
Calcular y mostrar la recaudación total.
Salir
Todo el desarrollo tiene que estar modularizado: ingreso de datos, validaciones de líneas y coches, generación y verificación de existencia de legajo, cálculos, etc.

"""
"""
3 lineas de colectivo: 5 coches cada una
    linea A: coche 1A / coche 2A / coche 3A / coche 4A / coche 5A
    linea B: coche 1B / coche 2B / coche 3B / coche 4B / coche 5B    
    linea C: coche 1C / coche 2C / coche 3C / coche 4C / coche 5C
 
Matriz de 3 x 5

[        Coche 1     Coche 2     Coche 3     Coche 4     Coche 5
linea A:    15
linea B:    20  
linea C:    30
]       

65 --> PERO ESTOS 65 SON DEL MISMO COCHE 1 PARA TODAS LAS LINEAS. CUANDO EN REALIDAD CADA LINEA TIENE SU COCHE. 
OJO A LA HORA DE INTEPRETAR LOS COCHES Y DEVOLVER DATOS PORQUE TENGO LAS 15 DIRECCIONES DE MEMORIA PARA LOS 15 COCHES. 


 Hay 15 choferes, uno para cada colectivo. 
 
Menu:
    Identificar chofer con legajo --> Legajo debe existir dentro de una matriz de legajo.
    Validar: Si el chofer existe, cargar la recaudacion del viaje indicando Linea : A / B / C y COCHE:
    El chofer : Puede cargar mas de una recaudacion por dia para distintas lineas y coches. No hay tope. 
    ----> "Desea cargar otra recaudacion"?
    Cada coche de cada linea puede tener varias recaudaciones -> No hay un tope. 

    TODOS LOS DATOS LOS CARGO, TENGO QUE BUSCAR EL LEGAJO EN UNA LISTA PARA VALIDARLO. 
 """

"""
los legajos son generados aleatoriamente pero sin repetir.
los legajos son 15
matriz_legajos = [001,002,003,004,005,006,007,008,009,010,011,12,13,14,15
]

Chofer = [
            [Linea A:   [Coche 1A:Recaudacion]
                        [Coche 2A:Recaudacion]
                        [Coche 3A:Recaudacion]
                        [Coche 4A:Recaudacion]
                        [Coche 5A:Recaudacion]
            ] 
            [Linea B:   [Coche 1B:Recaudacion]
                        [Coche 2B:Recaudacion]
                        [Coche 3B:Recaudacion]
                        [Coche 4B:Recaudacion]
                        [Coche 5B:Recaudacion]
            ] 
            [Linea C:   [Coche 1C:Recaudacion]
                        [Coche 2C:Recaudacion]
                        [Coche 3C:Recaudacion]
                        [Coche 4C:Recaudacion]
                        [Coche 5C:Recaudacion]
            ] 
            ]

"""


#0 - Valido que lo que pongo sea un int para ver el tema del legajo.


#1 - Creo el legajo


bandera_seguir = True
bandera_legajo_ingresado = False
legajo_aleatorio = crear_legajo_choferes(15)
print(legajo_aleatorio)

#ingreso_cantidad_lineas = get_int("Ingrese la cantidad de lineas de su empresa: ")
#ingreso_cantidad_coches = get_int("Ingrese la cantidad de coches de su empresa: ")
matriz = crear_matriz_lineas_coches(3,5)

while bandera_seguir :
    opcion = input("""
a.Ingrese el numero de legajo del chofer.
b.Seleccionar Linea y Coche para ingresar la recaudacion.
c.Mostrar la recaudación de todos los coches y líneas.
d.Calcular y mostrar recaudación por línea.
e.Calcular y mostrar recaudación por coche. 
f.Calcular y mostrar la recaudación total.
g.Salir
Ingrese su opcion: """)
    
    match opcion:
        case "a":
            print(legajo_aleatorio) #BORRAR ESTO LUEGO
            ingreso_legajo = get_int("Ingrese el numero de legajo del chofer: ")
            validacion_legajo = validar_reintentos_chofer(ingreso_legajo, legajo_aleatorio)
            bandera_legajo_ingresado = True
           
    if bandera_legajo_ingresado == True:
        match opcion:
            case "b":
                matriz_cargada = cargar_matriz(matriz)
                #Tiene que ingresar una linea, si la linea no esta dentro de la matriz, no me debe dejar ingresar un coche. 

                #Luego tiene que ingresar un coche. 
                
                #Se validan las dos con la misma. Hay que parametrizar.
                
            case "c":
                racaudacion = mostrar_recaudacion_cada_choche_linea(matriz)
            case "d":
                #d.Calcular y mostrar recaudación por línea.
                pass
            case "e":
                pass
            case "f":
                pass
            case "g":
                salida = input("¿Desea salir del programa? y/n: ")
                if salida == "y":
                    bandera_seguir = False
    else:
        mensaje = "Error. Primero debe ingresar un legajo existente."
        print(mensaje)

    system("pause")
    system("cls")