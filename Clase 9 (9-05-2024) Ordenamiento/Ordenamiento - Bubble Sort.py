array = [1,4,3,5,2]

for i in range(0, len(array) - 1):    #representa el pivote verde ->se ejecuta una vez. #Rango del 0 al 4
    print(f"{i}")
    for j in range (1, len(array)): #representa el pivote naranja (itera mas veces) --> se ejecuta varias veces.
        print(f"\t{j}") #la t para acomodarlo de otra manera. 


#FORMA CORRECTA: 
for i in range(0, len(array) - 1):    #representa el pivote verde ->se ejecuta una vez. #Rango del 0 al 4
    print(f"{i}")
    for j in range (i + 1, len(array)): #representa el pivote naranja (itera mas veces) --> se ejecuta varias veces.
        print(f"\t{j}") #la t para acomodarlo de otra manera. 



#Ordenar el array de menor a mayor. 
for i in range(0, len(array) - 1):
    for j in range (i + 1, len(array)):
        if array[i] > array [j] : #Si se cumple la condicion hago un swap
            #swap
            auxiliar = array[i]
            array[i] = array [j]
            array[j] = auxiliar

a = 4
b = 1

#Ordenar el array de mayor a menor
for i in range(0, len(array) - 1):
    for j in range (i + 1, len(array)):
        if array[i] < array [j] : #Si se cumple la condicion hago un swap
            #swap
            auxiliar = array[i] #Me guardo el primer valor en el swap
            array[i] = array [j] #Hago la comparacion y reasigno lo que tenia en el i con lo que me brinda j
            array[j] = auxiliar #Le paso lo que tenia en el swap (que era lo que tenia en el array[i])

a = 4
b = 1


#############Magia de Python###############

a, b = b, a #Asigna posicionalmente. Hace un set. Seteo de datos. 

#array[i], array[j] = array[j], array[i]

#USAR LA LOGICA DE PROGRAMACION!

#Investigar burbujeo mejorado!.
