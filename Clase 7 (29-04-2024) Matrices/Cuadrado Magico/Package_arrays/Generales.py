from .Validate import *
from .Input import *

def crear_matriz (filas: int, columnas: int) -> int | None :
    matriz = get_init(filas, columnas)
    matriz = [[0] * columnas for _ in range(filas)]
    return matriz

def cargar_matriz (matriz: int) :
    for i in range(len(matriz)): 
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input("Ingrese un número: "))

def es_cuadrado_magico(matriz):
    M = len(matriz)
    N = len(matriz[0])

    constante_magica = M * (M**2 + 1) // 2 #TIENE QUE DAR 15 SI O SI

    # filas y columnas
    for i in range(M):
        suma_fila = 0
        suma_columna = 0
        for j in range(N):
            #Evaluar la traza y la diagonal magica. 
            suma_fila += matriz[i][j]
            suma_columna += matriz[j][i]
        if suma_fila != constante_magica or suma_columna != constante_magica:
            return False
        
    return True

# if es_cuadrado_magico(matriz):
#     print("La matriz ingresada SI es un cuadrado mágico")
# else:
#     print("La matriz ingresada NO es un cuadrado mágico")

