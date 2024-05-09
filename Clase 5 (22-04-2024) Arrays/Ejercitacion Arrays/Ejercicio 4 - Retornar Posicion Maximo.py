#Lucas Elias Amarilla 

#Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
#Enteros negativos y positivos. OJO


def encontrar_posicion_maximo (lista: list) -> str:
    mensaje = "Ingrese un dato del tipo LISTA"
    primer_numero = True #Bandera
    if type(lista) is list:
        mensaje =  "La lista esta vacia"
        if len(lista) > 0 :
            maximo = None
            posicion_maximo = 0
            for i in range (len(lista)):
                if primer_numero == True or lista[i] > maximo:
                    primer_numero = False
                    maximo = lista[i] #Aca me guardo el valor de ese numero. 
                    posicion_maximo = i + 1
                mensaje = f"El numero maximo es: {maximo} y su posicion es: {posicion_maximo} en la lista."

    return mensaje



def encontrar_solamente_posicion_maximo (lista: list) ->int | bool :
    posicion_maximo = False
    primer_numero = True #bandera
    if type(lista) == list :
        posicion_maximo = True
        maximo = None
        if len(lista) > 0 :
            posicion_maximo = 0
            for i in range (len(lista)):
                if primer_numero == True or lista[i] > maximo : #Ojo aca porque quise evaluar las posiciones y no el valor del dato para luego obtener su posicion. 
                    primer_numero = False
                    maximo = lista[i]
                    posicion_maximo = i + 1
                    
    return posicion_maximo

lista = [1, 5, 2, 500, 2, 500, 200]
#posicion_maximo = encontrar_posicion_maximo(lista)
#print(posicion_maximo)

unicamente_posicion = encontrar_solamente_posicion_maximo(lista)

if unicamente_posicion == False :
    mensaje = "Ingrese un dato del tipo LISTA"
elif unicamente_posicion == True:
    mensaje = "La lista ingresada esta VACIA"
else :
    mensaje = f"La posicion del numero maximo es: {unicamente_posicion}"

print(mensaje)