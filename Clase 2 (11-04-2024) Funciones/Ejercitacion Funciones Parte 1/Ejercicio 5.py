#nombre: Lucas Elias Amarilla

#Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

def calcular_area_circulo (parametro: int) ->int : #En el parametro va el radio.
    numero_pi = 3.14
    radio = int(parametro)
    area_circulo = numero_pi * (radio * radio )
    return area_circulo

radio_ingresado = input("Ingrese el radio del circulo:")

area_calculada = calcular_area_circulo(radio_ingresado)
print(f"El area resultante es: {area_calculada}")