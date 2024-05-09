
matriz =[
    [5,4,9],
    [9,8,7],
    [3,1,5]
]

#Como recorro esta lista? Con 2 for la recorro. Necesito un for para las filas y un for para las columnas. Columnas: Valores de estas listas anidadas. 
# i representa las filas

#Por cada iteracion del for del afuera, va a reprensentar un for del adentro. 
x = 1
y = 2

#la matriz es de 3 por 3 y pongo dentro tengo esos valores. 3 filas y 3 columnas

for i in range (3):
    for j in range (3):
        pass
        #print(f"[{i}][{j}]")

#Tengo 3 iteraciones por cada vuelta. Me paro en las coordenadas, asi debo pensarlo : Batalla Naval.

"""
    0    1    2
0 - 5    4    9
1 - 9    8    7
2 - 3    1    5
"""
#----------------------------------------------------------------------------------------------------------#
for i in range (3):
    for j in range (3):
        print(matriz[i][j], end = " ") #i son las filas, j son las columnas.
        #end = " " --->SUPRIME EL SALTO DE LINEA. 
    print("") #para eliminar el salto de linea y me quede la matriz armada.

#Asi se printea en formato de matriz para no usar el print (matriz)
print(matriz)

#-------------------------------------------------------------------------------------------------------------#
#Es un tipo de dato dinamico. La matriz es una lista de listas, no me escapo de su concepto. 
"""
matriz = [[0] * 3 for _ in range (4)]

Voy a utilizar la comprension de listas. -> for _ in range. 
el for repite el proceso de [0] * 3 por 4 veces. 
Me da una matriz de 3 filas con 4 columnas. 
El "_" es una forma de llamar a la variable de control cuando no me interesa. En lugar de usar i, j, k, directamente como no la utilizo luego, pongo el _.





"""