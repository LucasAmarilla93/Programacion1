#Lucas Elias Amarilla

#Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.


def identificar_paridad (numero: int) -> str :
    numero = int(numero)
    if numero % 2 == 0:
        mensaje = "El numero es par"
    else:
        mensaje = "El numero es impar"
    return mensaje

numero_ingresado = input("Ingrese un numero: ")

numero_paridad = identificar_paridad (numero_ingresado)
print(numero_paridad)