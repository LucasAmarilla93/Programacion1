from .Validate import *

def contar_positivos (lista: list) -> str:
    contador_positivos = validate_int_positive(lista)
    if contador_positivos > 0:
        mensaje = f"La cantidad de numeros positivos encontrados es: {contador_positivos} "
    else: 
        mensaje = "No se encontraron numeros positivos."
    print (mensaje)

def contar_negativos (lista: list) -> str:
    contador_negativos = validate_int_negative(lista)  
    if contador_negativos > 0:
        mensaje = f"La cantidad de numeros negativos encontrados es: {contador_negativos}"
    else : 
        mensaje = "No se ingresaron numeros negativos."
    print (mensaje)

def crear_lista_nueva_paridad (lista: list) -> list: #Creo una nueva lista unicamente con los numeros pares. 
    lista_nueva = []
    for i in range (len(lista)): #Tengo que ver como crear una lista mas pequeña y que me tome solo los valores pares. Eliminando los 0 
        if lista[i] % 2 == 0 :
            lista_nueva.append(lista[i])
    return lista_nueva

def crear_lista_nueva_imparidad (lista: list) -> list: #Creo una nueva lista unicamente con los numeros pares. 
    lista_nueva = []
    for i in range (len(lista)): #Tengo que ver como crear una lista mas pequeña y que me tome solo los valores pares. Eliminando los 0 
        if lista[i] % 2 == 1 :
            lista_nueva.append(lista[i])
    return lista_nueva

def determinar_paridad (numero: int) -> bool:
    retorno = False
    if numero % 2 == 0 :
        retorno = True
    return retorno

def determinar_imparidad(numero: int) -> bool:
    retorno = False
    if numero % 2 == 1 :
        retorno = True
    return retorno

def determinar_longitud_pares (lista: list) -> int| None:
    contador_longitud_pares = 0
    for i in range (len(lista)):
        if lista[i] % 2 == 0:
            contador_longitud_pares +=1
    return contador_longitud_pares

def determinar_longitud_posiciones_impares (lista: list) -> int | None:
    longitud_lista_posiciones_impares = 0
    for i in range (len(lista)):
        if i % 2 == 1:
            longitud_lista_posiciones_impares += 1
    return longitud_lista_posiciones_impares