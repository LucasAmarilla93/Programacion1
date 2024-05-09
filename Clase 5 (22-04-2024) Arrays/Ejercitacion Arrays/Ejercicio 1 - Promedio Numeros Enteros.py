#Lucas Elias Amarilla

#Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.

def promediar_numeros_enteros (lista: list) -> int | float:
    promedio = None
    if type(lista) is list : #Verifico que si lo que ingreso es una lista. 
        suma_enteros = 0 #Inicializo la variable que acumula los enteros de la lista.
        for i in range(len(lista)): #recorro la lista y sumo los enteros. Una vez finalizado hago el promedio. 
           suma_enteros += lista[i]
        if suma_enteros != 0 :
            promedio = suma_enteros / (len(lista))
    return promedio

lista = [5, 10, 12 , 35, 20 ]

promedio_lista = promediar_numeros_enteros(lista)
print(f"El promedio de la lista es de: {promedio_lista}")