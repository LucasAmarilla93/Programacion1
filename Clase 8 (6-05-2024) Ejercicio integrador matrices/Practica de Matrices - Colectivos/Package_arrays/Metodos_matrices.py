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
    """_summary_Funcion que crea la matriz donde se guardaran todos los datos. 

    Args:
        filas_lineas (int, optional): Parametro de la cantidad de filas a crear. Esta en = Defaults to 3.
        coches_columnas (int, optional): Parametro de la cantidad de columnas a crear.Esta en = Defaults to 5.

    Returns:
        list: Retorna una lista con la cantidad de filas y columnas deseadas.
    """
    matriz = [[0] * coches_columnas for _ in range (filas_lineas)]
    return matriz 

def cargar_matriz (matriz: list) -> list:
    """_summary_Recibe como parametro la lista, la cual sera cargada con los llamados a ingreso_linea e ingreso_coche. 

    Args:
        matriz (list): Se recibe la matriz vacia a cargar.

    Returns:
        list: Devuelve la lista con los elementos cargados.  
    """
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
            #print(matriz[i][j], end= " ")
        #print("")
   
def mostrar_recaudacion_cada_choche_linea (matriz: list) -> list :
    """_summary_Muestra la recaudacion por cada coche de cada linea.

    Args:
        matriz (list): recibe la matriz cargada

    Returns:
        list: Devuelve la matriz printeada por consola con lo recaudado por cada coche de cada linea.
    """
    for i in range (len(matriz)):
        for j in range (len(matriz[0])):
            print(f"El coche {j + 1} de la linea {i + 1} recaudo: {matriz[i][j]} $")
        print ("")
                                    

 #d.Calcular y mostrar recaudación por línea. 
 #Es decir que yo tengo que recorrer cada linea e ir sumando los valores en un acumulador y printearlos.

def mostrar_recaudacion_linea (matriz: list) -> list:
    """_summary_Printea por consola la recaudacion por cada una de las lineas en su totalidad.

    Args:
        matriz (list): matriz ya cargada con datos.

    Returns:
        list: Printea la recaudacion de las lineas por consola
    """
    for i in range(len(matriz)):
        acumulador = 0 #el acumulador en cada iteracion del i debe reestablecerse a 0
        for j in range(len(matriz[0])):
            acumulador = matriz[i][j] + acumulador
        print(f"La linea {i + 1} recaudo: {acumulador}$")

def mostrar_recaudacion_coche (matriz: list) -> list:
    """
    _summary_Printea por consola la recaudacion por cada una de los coches en su totalidad.

    Args:
        matriz (list): matriz ya cargada con datos.

    Returns:
        list: Printea la recaudacion de los coches por consola
    """
    for j in range(len(matriz[0])):
        acumulador = 0
        for i in range(len(matriz)):
            acumulador = matriz [i][j] + acumulador
        print(f"El coche {j + 1} recaudo: {acumulador}$")

def mostrar_recaudacion_total (matriz: list) -> list:
    """_summary_Muestra la recaudacion de la totalidad de los ingresos.

    Args:
        matriz (list): recibe la matriz cargada por parametro.

    Returns:
        list: Devuelve la lista ya cargada. 
    """
    acumulador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            acumulador = matriz[i][j] + acumulador
    print(f"El total recaudado es: {acumulador}$")