MENSAJE = "HOLA A TODOS, BIENVENIDOS"


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
