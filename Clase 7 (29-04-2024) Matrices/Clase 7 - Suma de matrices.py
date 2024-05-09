matriz_a =[
    [5,4,9],
    [9,8,7],
    [3,1,5]
]

matriz_b =[
    [5,14,9],
    [19,8,17],
    [3,11,5]
]

M = len(matriz_a) #cantidad filas
N = len(matriz_a[0]) #cantidad columnas.

matriz_resultado = [[0]*N for _ in range (M)]

for i in range(M):
    for j in range (N):
        matriz_resultado[i][j] = matriz_a[i][j] + matriz_b[i][j]

for i in range (M):
    for j in range(N):
        print(f"{matriz_resultado[i][j]: 5}", end = " ")
    print("")