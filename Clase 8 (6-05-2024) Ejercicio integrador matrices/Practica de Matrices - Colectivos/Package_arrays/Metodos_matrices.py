import random
from .Input import *
def crear_legajo_choferes (numero: int) -> list:
    """summary: Crea una matriz donde se alojaran numeros(representando legajos) creados aleatoriamente

    Args:
        numero (int): recibe un int para determinar la cantidad de elementos de la matriz.

    Returns:
        list: retorna una lista con numeros creados aleatoriamente entre 1000 y 2000
    """
    legajo_choferes = [0] * numero
    for i in range(len(legajo_choferes)):
        legajo_choferes[i] = random.randint(1000,2000)
    return legajo_choferes


def crear_matriz_lineas_coches (filas_lineas = 3, coches_columnas = 5) -> list:
    matriz = [[0] * coches_columnas for _ in range (filas_lineas)]
    return matriz 

def cargar_matriz (matriz: list) -> list | bool:
    ingreso_linea = get_int("Ingrese el numero de linea: ")
    validacion_rango_linea = validar_rango("La linea no existe en el registro. Reingrese otra linea: ",ingreso_linea, 1, 3)
    ingreso_coche = get_int("Ingrese el numero coche: ")
    validacion_rango_coche = validar_rango("El coche no existe en el registro. Reingrese otro coche: ",ingreso_coche, 1, 5)
    ingreso_recaudacion = get_int("Ingrese el monto recaudado: ")
    
    #el acumulador es la suma de lo del input, mas lo que haya en esas coordenadas de la matriz. De no tener nada, la suma es nula.
    acumulador = ingreso_recaudacion + matriz[validacion_rango_linea - 1][validacion_rango_coche - 1]
    #Sumo lo que me pasan por input mas lo que haya en esas posiciones de [i] y de [j]
    #Al recorrerse se va sumando el acumulador y evaluando lo que habia antes previamente sin pisarlo, ni sumarlo demas en cada iteracion. 

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            #acumulo lo que ingreso, mas lo que haya en esas coordenadas.
            matriz[validacion_rango_linea - 1][validacion_rango_coche - 1] = acumulador #Esto no me acumula los resultados sino que me los pisa. 
            print(matriz[i][j], end= " ")
        print("")
   
def mostrar_recaudacion_cada_choche_linea (matriz: list) -> list :
    for i in range (len(matriz)):
        for j in range (len(matriz[0])):
            print(f"El coche {j + 1} de la linea {i + 1} recaudo: {matriz[i][j]} $")
        print ("")
                                    