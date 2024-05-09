
def determinar_cuadrado_magico(matriz:list) -> bool:
    """Determinar si es cuadrado magico

    Args:
        matriz (list): Verifica mediante la constante mágica si es o no un cuadrado mágico

    Returns:
        bool: True si es cuadrado magico | False si NO es cuadrado magico 
    """
    # filas y columnas
    M = len(matriz)
    N = len(matriz[0])

    # variables y formula
    constante_magica = M * (M**2 + 1) / 2 
    retorno = False    
    traza = 0
    diagonal_inversa = 0
   
    for i in range(M):
        suma_fila = 0
        suma_columna = 0
    
        for j in range(N):
            # filas y columnas
            suma_fila += matriz[i][j]
            suma_columna += matriz[j][i]
            # diagonal principal
            if i == j :
                traza += matriz[i][j]
            # diagonal secundaria
            if i + j == M - 1:
                diagonal_inversa += matriz[i][j]
  
    # compara la suma con la formula de la constante mágica
    if suma_fila == constante_magica and suma_columna == constante_magica and traza == constante_magica and diagonal_inversa == constante_magica:
        retorno = True

    return retorno

# pide datos al usuario
M = int(input("Ingrese la cantidad de filas: "))
N = int(input("Ingrese la cantidad de columnas: "))

while M != N or M < 3 or N < 3:
    M = int(input("Error. Reingrese la cantidad de filas: "))
    N = int(input("Error. Reingrese la cantidad de columnas: "))

matriz = [[0] * N for _ in range(M)]
for i in range(len(matriz)): 
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f"Ingrese un número en {i},{j}: "))

# verifica si es o no un cuadrado mágico
if determinar_cuadrado_magico(matriz) == True:
    mensaje = "La matriz ingresada SI es un cuadrado mágico"
else:
    mensaje = "La matriz ingresada NO es un cuadrado mágico"
print(mensaje)

#ejemplo de cuadrado magico: 8 1 6 3 5 7 4 9 2
# 6 13 8 11 9 7 10 5 12
