def validate_int (numero: int, minimo = -1000, maximo = 1000) -> int :
    #Yo quiero validar que el numero sea entero entre -1000 y 1000
    while numero < minimo or numero > maximo :
        numero = input("Error. Reingrese un numero entero dentro del rango: -1000, 1000: ")
        numero = int(numero)
    return numero    

def validate_int_negative (lista: list) -> int:
    contador_negativos = 0
    for i in range (len(lista)):
        if lista[i] < 0 :
            contador_negativos += 1
    return contador_negativos

def validate_int_positive (lista: list) -> int: 
    contador_positivos = 0
    for i in range (len(lista)):
        if lista[i] > 0 :
            contador_positivos += 1
    return contador_positivos

def validate_list (lista: list) -> list | None:
    retorno = None
    if type(lista) is list and len(lista) > 0 :
        retorno = lista
    else:
        retorno = False
    return retorno
