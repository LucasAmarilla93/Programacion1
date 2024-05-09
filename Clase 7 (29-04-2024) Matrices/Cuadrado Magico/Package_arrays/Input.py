from .Validate import *

def get_init (filas: int, columnas: int) -> int | None :
    filas = input("Ingrese cantidad de filas: ")
    columnas = input("Ingrese la cantidad de columnas: ")
    validacion_cuadrado = validar_cuadrado_magico(filas,columnas)
    return validacion_cuadrado