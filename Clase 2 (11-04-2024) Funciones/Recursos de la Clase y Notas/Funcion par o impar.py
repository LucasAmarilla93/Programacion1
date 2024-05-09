#Y que devuelva el resultado en string -->transformado.

def determinar_numero_par(numero_ingresado): #como le puse a mi parametro, es con lo que trabajo. Recibe la cantidad de parametros que ponga. 
    if numero_ingresado % 2 == 0 :
        mensaje = "El resultado es par"
    else :
        mensaje = "El resultado es impar"
    return mensaje
#No me sirve devolverle el numero que me dio, me sirve ver si es par o no, nada mas

parametro = input("Ingrese un numero") #ingreso el dato
parametro = int(parametro) #lo casteo a numero
resultado = determinar_numero_par(parametro) #ejecuto la funcion
parametro = str(parametro) #lo casteo a str porque pidio que el resultado sea un str.  

print(f"{resultado, parametro}")
print(type(parametro))

