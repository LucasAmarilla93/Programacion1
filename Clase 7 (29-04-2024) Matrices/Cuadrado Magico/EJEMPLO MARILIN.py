def cuadrado_magico(matriz):
    filasA = len(matriz) #es el largo de la matriz.
    columnasA = len(matriz)
    constante_magica = filasA * (filasA ** 2 + 1) / 2
    retorno = True
    # filas y columnas
    for i in range(filasA):
        suma_diagonal = 0
        suma_diagonal_inversa = 0
        suma_fila = 0
        suma_columna = 0
        for j in range(columnasA):
            suma_fila += matriz[i][j]
            # print(f"suma i: {suma_fila}")
            suma_columna += matriz[j][i]
            # print(f"suma columnas: {suma_columna}")
            #diagonal principal. 
            if i == j:
                suma_diagonal += matriz[i][j]
               
            if i + j == filasA -1:
                suma_diagonal_inversa += matriz[i][j]
            # mostramos la matriz completa 
            print(f"{matriz[i][j]:5}",end = " ")
        print("")   
                
    if constante_magica != suma_diagonal or constante_magica != suma_columna or constante_magica != suma_fila or constante_magica != suma_diagonal_inversa:
        retorno = False
    return retorno


#PIDES DATOS AL USUARIO
print("ingresa el orden de la matriz a calcular");

filasA, columnasA = int(input()),int(input()); # 3 x 3  

if filasA == columnasA:
    matriz = [[0] * columnasA for _ in range(filasA)]
    
    for fila in range(filasA):
        for columna in range(columnasA):
            matriz[fila][columna] = int(input(f"ingrese la posicion numero {fila}, {columna}: "))
                  
        
    # verifica si es o no un cuadrado mágico
    if cuadrado_magico(matriz):
        print("La matriz ingresada SI es un cuadrado mágico")
    else:
        print("La matriz ingresada NO es un cuadrado mágico")
 
else:
   print("La matriz no es cuadrada")