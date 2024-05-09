#Lucas Elias Amarilla

#Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

def calcular_posiciones_maximos (lista: list) -> int | bool:
#    retorno = False
    bandera_primer_numero = True
#    if type(lista) is list:
#        retorno = True
#        if len(lista) > 0 :
#            maximo = None
#            posicion = None
    for i in range(len(lista)):
        if bandera_primer_numero == True :
            maximo = lista [i]
            posicion = i + 1  #Necesito ir guardandome las posiciones o ir imprimiendolas por consola. 
            bandera_primer_numero = False
        elif lista[i] > maximo : 
            maximo = lista [i] #Cambio el valor a maximo
            posicion = i + 1   #Me guardo la posicion de ese maximo
            
    for j in range(len(lista)):
        if lista[j] == maximo:
            posicion = j + 1
            print(posicion)
   
lista = [100, 5, 100, 8, 100, 50, 15]

calculo_posiciones = calcular_posiciones_maximos(lista)
#print(calculo_posiciones)
