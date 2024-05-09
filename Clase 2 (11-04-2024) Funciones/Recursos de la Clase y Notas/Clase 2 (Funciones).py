import random
"""""
Quiero sumar dos numeros y que esos numeros se los pida al usuario.
un_numero = input ("Ingrese un numero")
un_numero = int(un_numero)
otro_numero = input ("Ingrese un numero")
otro_numero = int(otro_numero)

suma = un_numero + otro_numero

print(f"La suma es: {suma}")
"""""
#-----------------------------------------------------------------------------------------------------#

#Ahora quiero crear una funcion con dicho algoritmo

#Instancia del desarrollo de una funcion.

#CTRL + CLICK DERECHO ME LLEVA A DONDE ESTA LA FUNCION
def sumar_1(): #Caso planteado donde pido los numeros dentro de una funcion ---> NO ESTA BIEN!!!.
    un_numero = input ("Ingrese un numero")
    un_numero = int(un_numero)
    otro_numero = input ("Ingrese un numero")
    otro_numero = int(otro_numero)

    suma = un_numero + otro_numero

    print(f"La suma es: {suma}")

def sumar_2(un_numero, otro_numero): #Caso donde recibe por parametro los 2 numeros que yo quiero sumar. Los numeros que quiero sumar vienen parametrizados. 
    suma = un_numero + otro_numero

    print(f"La suma es: {suma}")


def sumar_3():
    un_numero = input ("Ingrese un numero")
    un_numero = int(un_numero)
    otro_numero = input ("Ingrese un numero")
    otro_numero = int(otro_numero)

    suma = un_numero + otro_numero

    return suma


def sumar_4(un_numero, otro_numero): #Aca ingreso cuantos parametros quiero poner, no que parametros estoy llamando justamente. 
    suma = un_numero + otro_numero
    
    return suma

#----------------------------------------------------------------------------#

#Instancia de invocacion de una funcion. --> Llamada de una funcion. //Para ejecutarla la tengo que llamar implicitamente. 
#print("Bienvenido a mi programa")
#sumar_1() #No recibe parametros y NO DEVUELVE NADA -->Funcion altamente cohesiva pero es NULA. No la puedo reutilizar porque por ejemplo no puedo sumar dos aleatorios. Encima hace un monton de cosas. No puedo retornarlo por otro lado porque no me retorna nada la funcion.
#print("Fin del programa")

#-----------------------------------------------------------------------------#

#sumar_2(8,9)

#-----------------------------------------------------------------------------#
#Aca le pido al usuario previamente que ingrese los numeros. 
#un_numero = input ("Ingrese un numero")
#un_numero = int(un_numero)
#otro_numero = input ("Ingrese un numero")
#otro_numero = int(otro_numero)
#sumar_2(un_numero, otro_numero)

#------------------------------------------------------------------------------#
#Le paso dos numeros aleatorios
#un_numero = random.randint(1,100)
#otro_numero = random.randint(500,700)

#sumar_2 (un_numero, otro_numero) #Recibe parametros pero NO devuelve nada. 

#-------------------------------------------------------------------------------#

#sumar_3() No es independiente con respecto a la entrada de datos pero si es independiente a la salida de los mismos.
#resultado = sumar_3() #Retorna algo y yo tengo que atajarlo de alguna manera. Tengo que guardar el resultado de la funcion dentro de una variable para atajar dicho resultado!.
#print(f"La suma es : {resultado}")

#---------------------------------------------------------------------------------#

#Esta funcion recibe numeros y no le interesa de donde vienen, hace lo que tiene que hacer y retorna lo que tiene que retornar, no le interesa para donde va lo que retorna. Es una funcion independiente y reutilizable. 

un_numero = input ("Ingrese un numero")
un_numero = int(un_numero)
otro_numero = input ("Ingrese un numero")
otro_numero = int(otro_numero)

resultado = sumar_4(un_numero, otro_numero) #Recibe parametros y retorna el resultado. Los parametros en este caso ya estan ingresados por otro lado. Obviamente tengo que guardar la suma del resultado en una variable. 

print(resultado)
  

#LAMBDA --> Quiero una funcion que se ejecuta una sola vez. Es una funcion anonima.

#En sumar_1() Tengo un error, es muy dificil parcearla porque en dicha funcion tengo: Ingreso de un numero, ingreso de otro numero, la suma de ambos y ademas LO PRINTEO. Son demasiadas acciones en un codigo que esta junto y se vuelve dificil ver realmente donde esta el error. 

#CTRL K C para comentar todo. 