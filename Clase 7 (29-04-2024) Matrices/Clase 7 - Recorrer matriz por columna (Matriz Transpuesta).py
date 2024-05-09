matriz =[
    [5,4,9,10],
    [9,8,7,15],
    [3,1,5,11]
]


#len(matriz) recorre por fila.
#yo quiero recorrerlo por columna. 
#suponiendo que la matriz tiene la misma cantidad de columnas en todas las filas puedo utilizar el indice: 0
#De cualquier fila, decime el largo, si pongo 0


#Estoy "Dando vuelta la matriz" -> concepto de matriz transpuesta. 

def imprimir_matriz (lista: list) -> list:
    for j in range(len(matriz[0])): #4
        #Me aseguro que hay una fila, de esa fila dame el largo: 0,1,2,3. Me da la cantidad de columnas. Para recorrer la columna me tengo que meter en cada uno de los elementos de la lista. 
                
        for i in range (len(matriz)): #3
            #Aca necesito la cantidad de filas, utilizo directamente el len(matriz)
            print (f"{matriz[i][j]:5}", end = " ")
        print("") #para que se muestre en formato matriz
        
#por cada valor de j yo itero 3 veces en i. 

matriz_impresa = imprimir_matriz(matriz)