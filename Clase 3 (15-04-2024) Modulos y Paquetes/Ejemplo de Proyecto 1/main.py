# import funciones -->"Importame el modulo"
# #Siempre que importo un modulo, debo utilizar el nombre del modulo y hacer la llamada explicita de la funcion.

# funciones.sumar_2(2,5)
# resultado = funciones.sumar_3() //--> Me obliga a utilizar el nombre del modulo adelante si o si. 
# print(resultado)

#/////////////////////////////////////////////////////////////////////////////////////////////

# from funciones import * #-->significa "De funciones importame TO DO" "Desde el modulo funciones, importa todo"

# print(MENSAJE)

# resultado = sumar_4(9,9)

# print(resultado)

#////////////////////////////////////////////////////////////////////////////////////////////////

#Si tengo 500 funciones y quiero traer algunas especificas hago lo siguiente.

#from Package_Funciones.funciones import sumar_2 #Solo me traigo la funcion de sumar_2() del modulo funciones que esta en el paquete FUNCIONES.

#Si esta en un paquete tengo que importa el modulo que esta en el paquete. 

#sumar_2(4,9)

#////////////////////////////////////////////////////////////////////////////////////////////////

# import Package_Funciones.funciones as SUMAR #--> con el as lo redifino todo como si fuese un alias y lo llamo desde ahi.  

# SUMAR.sumar_4()


# #///////////////////////////////////////////////

# from random import randint, choice #-->importo unicamente lo que necesito. 


# numero = randint(1,9)

# print(numero)

# lista_opciones = ["verde", "roja", "azul", "amarillo"]

# opcion = choice(lista_opciones)

# print(opcion)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def get_int() -> int: #get_int por una cuestion de convencion, lo que conviene es programar en ingles. 
    numero = input("Ingrese su numero: ") 
    numero = int(numero)

    return numero

#asigno la funcion a una variable

# numero_solicitado = get_int()

# print(f"El numero ingresado es: {numero_solicitado}")

#Quiero pedir al usuario que ingrese: edad, legajo y nota. 
#Si reutilizo siempre lo mismo, no va. 

edad = get_int()
legajo = get_int()
nota = get_int()

#En esta opciones, me molesta el texto, porque dice numero. Entonces tengo que ir parametrizandolo.
#Entonces lo cambio a esta forma para PARAMETRIZARLA:

def get_int(mensaje: str) -> int: #get_int por una cuestion de convencion, lo que conviene es programar en ingles. 
    numero = input(mensaje) 
    numero = int(numero)

    return numero

edad = get_int("Ingrese su edad: ") 
legajo = get_int("Ingrese su legajo: ")
nota = get_int("Ingrese su nota: ")

#////////////////////////////////////////////////////////////////////////////////////////////#

#Quiero validar datos de manera antigua. El tema es que es demasiado repetitivo. Porque el tipo de dato y el compartimiento es identico.

edad = get_int("Ingrese su edad: ") # quiero un rango entre 18-30 para validarlo. 
while edad < 18 or edad > 30 :
    edad = get_int("Error. Ingrese su edad: ")

legajo = get_int("Ingrese su legajo: ") # 1000-2000
while legajo < 1000 or legajo > 2000 :
    legajo = get_int("Error. Ingrese su legajo: ")

nota = get_int("Ingrese su nota: ") # 1 - 10
while nota < 1 or nota > 10 :
    nota = get_int("Error. Ingrese su nota: ")

# SOLUCION 
def get_int(mensaje: str, minimo: int, maximo: int) -> int:
    numero = input(mensaje) 
    numero = int(numero)
    while numero < minimo or numero > maximo :
        numero = input(f"Error.{mensaje}") #recursividad
        numero = int(numero)
    return numero

#La llamada a funcion quedo limpia.  Sirve para pedir cualquier variable de tipo entera y para validarla en un rango.

edad = get_int("Ingrese su edad: ", 18, 30) # quiero un rango entre 18-30 para validarlo. 
#if (edad!=none): --->pido datos, sino finaliza el programa. 
legajo = get_int("Ingrese su legajo: ", 1000, 2000) # 1000-2000

nota = get_int("Ingrese su nota: ", 1 , 10) # 1 - 10
