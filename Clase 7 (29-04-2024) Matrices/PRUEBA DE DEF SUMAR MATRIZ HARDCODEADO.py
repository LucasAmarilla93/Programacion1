matriz_ejemplo =[
    [5,4,3],
    [9,8,100]

]

def sumar_matriz (matriz: list) -> list:
    suma_fila = 0
    acumulador_resultado = [0] * 2
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if i == 1:
                suma_fila += matriz[i][j]
                print(f"La suma de la fila es: {suma_fila}")
                acumulador_resultado [i] = suma_fila
                print(f"la lista es {acumulador_resultado}")
            else :
                suma_fila += matriz[i][j] #me toma el valor anterior de la suma fila. 
                acumulador_resultado [i] = suma_fila
                print(f"la lista es {acumulador_resultado}")

    print(f"Suma de fila: {suma_fila}")
    print(f"la fila dos es {suma_fila}")

suma = sumar_matriz(matriz_ejemplo)