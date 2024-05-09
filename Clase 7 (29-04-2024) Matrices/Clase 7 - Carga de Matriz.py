M = 3 #filas
N = 3 #columnas

matriz = [[0] * N for _ in range (M)]

for i in range (len(matriz)): 
    for j in range (len(matriz[i])): #con estos 2 for puedo recorrer la matriz. 
        matriz[i][j] = int(input("Ingrese un numero: ")) #Ojo aca porque si solo pongo matriz[i] me va a colocar en todo el i y no en el i dentro del j. 
        #cada vez que me meta dentro de la matriz voy a necesitar la posicion de i acompañada de j para pararme dentro de un elemento.


#ESTO QUEDA TURULECO
for i in range (len(matriz)): 
    for j in range (len(matriz[i])): 
        print(matriz[i][j], end = " ") #Esto se rompe porque un entero no tiene largo. 
    print("") #Si el numero es grande, queda turuleco.

#ESTO QUEDA MEJOR
for i in range (len(matriz)): 
    for j in range (len(matriz[i])): 
        print(f"{matriz[i][j]:5}", end = " ") #Esto no se desfaza porque lo tengo a la izquierda 5 caracteres, le doy un parametro. 
    print("") #Si el numero es grande, ahora queda bien.


