#Pido un numero por consola. 
#El mensaje es el que va a imprimir antes de pedirle al usuario el dato por consola.


def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    numero = input(mensaje)
    numero = int(numero)
    reintentos_realizados = 0
    #Cada vez que yo valido un dato, suma una unidad mas al reintento, al llegar a la cantidad identica, se corta la ejecucion. 

    while numero < minimo or numero > maximo: #Llamo de nuevo a input aca en esta validacion. Recursividad?
        if reintentos_realizados != reintentos: #Hay reintentos?
            numero = input(f"{mensaje_error}") 
            numero = int(numero)
            reintentos_realizados +=1
        else:
            numero = None
            break
    #De esta manera unicamente me toma 2 de los 3 reintentos. 

    return numero

#dato = get_int("Ingrese un numero entero: ", "Error. Reingrese otro numero ", 1, 100, 3)
#año = get_int("Ingrese un año:" ,"Error", 1900, 2000 , 2 )
#print(dato)


def get_float(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> float | None:
    numero_flotante = input(mensaje)
    numero_flotante = float(numero_flotante)
    contador_reintentos = 0

    while numero_flotante < minimo or numero_flotante > maximo:
        if contador_reintentos != reintentos :
            numero_flotante = input(mensaje_error)
            numero_flotante = float(numero_flotante)
            contador_reintentos += 1 
        else:
            numero_flotante = None
            break

    return numero_flotante


#dato_float = get_float ("Ingrese un numero flotante:", "Error. Reingrese otro numero: ", 1, 10, 3)  


def get_string(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> str | None:
    cadena_ingresada = input(mensaje)
    cadena_cantidad_caracteres = len(cadena_ingresada)
    contador_reintentos = 0 #Cuento los reintentos para hacer el break
    while cadena_cantidad_caracteres < minimo or cadena_cantidad_caracteres > maximo : 
        cadena_ingresada = input(mensaje_error)
        cadena_cantidad_caracteres = len(cadena_ingresada)
        contador_reintentos += 1

        if contador_reintentos == reintentos : 
            cadena_ingresada = None
            break
    
    return cadena_ingresada



dato_string = get_string("Ingrese un string: ", "Error. Reingrese otro string: ", 1 , 12, 3)
print(dato_string)

    
#El VALIDATE SOLO SE VALIDA EL RANGO SI VA O NO
#INPUT SE DESARROLLA TODA LA FUNCION. 

#HAY QUE DOCUMENTAR LAS FUNCIONES!!!!