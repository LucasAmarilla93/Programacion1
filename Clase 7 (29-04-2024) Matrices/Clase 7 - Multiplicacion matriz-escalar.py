#Multiplicacion matriz - escalar.
#El producto de una matriz me da otra matriz con otros resultados.

#trabajo con 2 matrices, un factor y el elemento del resultado.
"""
"""
matriz =[
    [5,4,9],
    [9,8,7],
    [3,1,5]
]

escalar = 5

#Quiero multiplicar toda la matriz por el valor. 
#Necesito una nueva matriz donde guardar esto, creo la matriz resultado.

M = len(matriz) #filas
N = len(matriz[0]) #columnas


matriz_resultado = [[0] * N for _ in range(M)]  
#va len de matriz porque si pongo una fila mas se me rompe.
#va len(matriz[0]) para saber la dimension de las columnas de la matriz.
#tiene que tener la misma cantidad de elementos de la original por la que voy a multiplicar.

#me conviene recorrer la matriz cargada para luego ir rellenandola en la matriz resultado.

for i in range(M):
    for j in range (N):
        matriz_resultado[i][j] = matriz[i][j] * escalar

for i in range(M):
    for j in range(N):
        print(f"{matriz_resultado[i][j]:5}", end = " ")
    print("")
