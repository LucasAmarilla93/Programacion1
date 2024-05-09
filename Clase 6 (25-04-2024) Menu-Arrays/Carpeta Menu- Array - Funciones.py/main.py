from os import system
from Package_Arrays.Input import *
from Package_Arrays.Especificas import *
from Package_Arrays.Arrays_Generales import *
from Package_Arrays.Validate import *
#Si puedo meterlo dentro de una funcion. lo hago.

"""Realizar un menú de opciones en donde el usuario pueda realizar las siguientes operaciones:
1-Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
2-Mostrar la cantidad de números positivos y negativos.
3-Mostrar la sumatoria de los números pares.
4-Informar el mayor de los números impares.
5-Listar todos los números ingresados.
6-Listar todos los números pares.
7-Listar los números de las posiciones impares.  
8-Salir

Notas:
Solo se podrá ingresar a las opciones b a g, siempre y cuando el usuario haya ingresado los datos solicitados.
T
odas las opciones deberán ser programadas en funciones: habrá funciones específicas (por ejemplo para determinar si un número es positivo o negativo) y funciones de nivel general (por ejemplo una función que liste los números pares). 

Tener en cuenta las características de la programación funcional.

Las funciones específicas deberán estar en el módulo “Especificas.py”, mientras que las generales en el módulo “Array_Generales.py”. Todos estos módulos deben estar integrados en el paquete Package_Arrays.

Utilizar las funciones input del paquete Package_Input.

"""

#Menu de opciones

bandera_seguir = True
bandera_ingreso_int = False
while bandera_seguir: 
    opcion = input("""  
a.Ingrese 10 numeros enteros entre -1000 y 1000: 
b.Mostrar la cantidad de numero positivos y negativos.
c.Mostrar la sumatoria de los numeros pares.
d.Informar el mayor de los numeros impares.
e.Listar todos los numeros ingresados
f.Listar todos los numeros pares.
g.Listar todos los numeros de las posiciones impares.
h.Salir
Ingrese su opcion: """ )
        
    match opcion :
        case "a": 
            ingreso_numeros = ingresar_int("Ingrese un numero entre -1000 y 1000: ")
            bandera_ingreso_int = True 

    if bandera_ingreso_int == True:     
        match opcion:
            case "b":
                positivos = contar_positivos(ingreso_numeros)
                negativos = contar_negativos(ingreso_numeros)
            case "c":
                paridad = acumular_paridad(ingreso_numeros)
                print(paridad)
            case "d": 
                maximo_imparidad = encontrar_maximo_imparidad(ingreso_numeros)
                print(maximo_imparidad)
            case "e":              
                lista_ingresada = mostrar_lista_numeros_ingresados(ingreso_numeros)
            case "f":
                lista_par = listar_numeros_pares(ingreso_numeros)
                print(lista_par)
            case "g":
                lista_posiciones_impares = listar_posiciones_impares(ingreso_numeros)
            case "h": 
                salir = input("¿Desea salir del programa? y/n: ")
                if salir == "y":
                    bandera_seguir = False
    else:
        mensaje = ("Error. Primero debe ingresar a la opcion: A para cargar datos.")
        print(mensaje)
    
    system("pause")
    system("cls")    


#FALTA VER EL CASO DE SI LE PASO UNA LISTA CON TODOS SUS VALORES EN 0