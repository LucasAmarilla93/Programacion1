#Crear una función que reciba una cadena y un caracter. La función deberá devolver el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.

def encontrar_caracter (cadena: str, caracter: str) -> int:
    caracter_indexado = -1
    for i in range (len(cadena)):
        if cadena[i] == caracter:
            caracter_indexado = i + 1
    return caracter_indexado



busqueda = encontrar_caracter("Hola? como= te va?", "1")

print(busqueda)