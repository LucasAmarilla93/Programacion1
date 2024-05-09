
# M = n*(n.2 + 1) / 2
# M = 3 *(3*2 + 1) / 2
# M = 3 * (7) / 2
# M = 10.5
#Un cuadrado mágico es una matriz cuadrada en la que la suma de los números en cada fila, cada columna y cada diagonal principal es la misma. Esto se conoce como constante mágica del cuadrado.
#La misma se calcula: 
#M = n*(n2 + 1)/2
#Formalmente, un cuadrado mágico de orden n, es una matriz cuadrada de nxn donde los números enteros del 1 al n2  están dispuestos de tal manera que la suma de los números en cada fila, cada columna y cada diagonal principal es igual a la misma constante mágica.
#Deberán desarrollar un programa que determine si el cuadrado de valores ingresado por el usuario es o no un cuadrado mágico. Tener en cuenta todas las validaciones posibles."

matriz_ejemplo =[
    [5,4],
    [9,8]
]

matriz_cuadrado_magico = [
    [8,1,6],
    [3,5,7],
    [4,9,2]
]

M = int(input("Ingrese la cantidad de filas: "))
N = int(input("Ingrese la cantidad de columnas: "))

while N != M :
    M = int(input("Error.Reingrese la cantidad de filas: "))
    N = int(input("Error.Reingrese la cantidad de columnas: "))

#Creo la matriz,
matriz  = [[0]* N for _ in range(N)]


#Funcion para imprimir la matriz
def imprimir_matriz (lista: list) -> list:
    for i in range (len(lista)):
        for j in range (len(lista[i])):
            print(f"{lista[i][j]:5}", end = " ")
        print("")
#matriz_impresa = imprimir_matriz(matriz)

#Funcion para cargar la matriz

def cargar_matriz(matriz: list) -> list:
    for i in range (len(matriz)):
        for j in range(len(matriz [i])):
            matriz[i][j] = int(input("Ingrese un numero"))

# Sumar cada fila y columna

def sumar_matriz (matriz: list) -> list:
    suma = 0
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            suma += matriz[i][j]
            return suma 

suma = sumar_matriz(matriz_ejemplo)
print(f"{suma:5}", end = " ")