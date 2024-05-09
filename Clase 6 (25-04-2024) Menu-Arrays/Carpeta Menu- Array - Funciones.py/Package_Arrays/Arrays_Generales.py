from .Especificas import *
from .Input import *

def crear_lista (numero = 0, tamaño_lista = 10) ->  list :
    lista = [numero] * tamaño_lista
    return lista
   
def ingresar_int (mensaje: str) -> int :   
    lista_creada = crear_lista()
    for i in range(len(lista_creada)): 
        dato_int = get_int(mensaje)
        lista_creada[i] = dato_int 
    return lista_creada

def acumular_paridad (lista: list) -> int: 
    acumulador = 0
    for i in range (len(lista)):
        if determinar_paridad(lista[i]) == True:
            acumulador += lista[i]
    return acumulador

def encontrar_maximo_imparidad (lista: list) -> int: 
    maximo_impar = -1001 #Ingreso un numero fuera del rango, o irracional a los parametros para que funcione. 
    bandera_primer_maximo = True
    for i in range (len(lista)):
        if determinar_imparidad(lista[i]) == True:
            if bandera_primer_maximo == True or lista[i] > maximo_impar:
                maximo_impar = lista [i] 
                bandera_primer_maximo = False
        else:
            if maximo_impar == -1001 :
                maximo_impar = "No hay impares" 
    return maximo_impar

def mostrar_lista_numeros_ingresados (lista: list) -> list:
    lista_validada = validate_list(lista)
    if lista_validada != False :
        mensaje = f"{lista_validada}"
    else:
        mensaje = f"No hay una lista ingresada para mostrar"
    print(mensaje)

def listar_numeros_pares (lista: list) -> list|None:
    retorno = []
    for i in range(len(lista)):
        if determinar_paridad(lista[i]) == True:
            retorno.append(lista[i])
    return retorno

def listar_posiciones_impares (lista: list) -> list | None:
    retorno = []
    for i in range (len(lista) + 1):
        if determinar_imparidad (i) == True:
            retorno.append(lista[i - 1])
    print (retorno)