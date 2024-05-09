from .Validate import *

def get_int(mensaje: str) -> int :  
    numero = input(mensaje)
    numero = int(numero)
    validacion = validate_int(numero)
    return validacion
