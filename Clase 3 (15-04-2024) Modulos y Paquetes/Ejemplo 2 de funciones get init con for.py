#Pido un numero por consola. 
#El mensaje es el que va a imprimir antes de pedirle al usuario el dato por consola.


def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    numero = input(mensaje)
    numero = int(numero)
    #Cada vez que yo valido un dato, suma una unidad mas al reintento, al llegar a la cantidad identica, se corta la ejecucion. 

    
    for i in range (reintentos) :
        while numero < minimo or numero > maximo: #Llamo de nuevo a input aca en esta validacion. 
            numero = input(mensaje_error)
            numero = int(numero)
            
    return numero

dato = get_int("Ingrese un numero: ", "Error. Reingrese otro numero ", 1, 10, 3)
print(dato)