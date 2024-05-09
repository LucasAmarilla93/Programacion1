# M * N habla del rango de la matriz.

M = 4 #filas
N = 3 #columnas

#matriz MxN 
#SIEMPRE ES EN EL ORDEN FILAS Y LUEGO COLUMNAS

matriz = [[0] * N for _ in range (M)]
#Cada elemento que quiero que tenga la fila, estoy hablando de cada columna. [0] * x es la FILA.
#for in range es la q de veces que se cree esta creacion de 3 jueguitos, que se cree 3 veces.

for i in range (M):
    for j in range (N):
        print(matriz[i][j], end = " ") 
    print("") 



#Esto me permite que el bucle no se me rompa. 
for i in range (len(matriz)): # representa el 4, porque tengo 4 filas en la matriz general.
    for j in range (len(matriz[i])): 
        #o poner len(matriz[0])
        # pongo len(matriz(i)) con una cantidad DISPARES DE COLUMNAs
        #Necesito la q de columnas de la matriz. 
        print(matriz[i][j], end = " ") 
    print("") 


