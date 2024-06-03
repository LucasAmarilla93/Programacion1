from Validate import *

def get_str (mensaje: str, mensaje_error : str) -> str | None:
    cadena = input(mensaje)
    validacion = validate_str(cadena, mensaje_error)
    return validacion

def get_int (mensaje: str, mensaje_error: str) -> int:
    numero = input(mensaje)
    validacion = validate_int(numero, mensaje_error)
    return validacion

def get_trazo(mensaje: str, mensaje_error: str) -> str:
    trazo = input(mensaje)
    lista_trazos = ["grueso", "fino"]
    validacion = validate_lista(trazo, mensaje_error, lista_trazos)
    return validacion

def get_color(mensaje: str, mensaje_error: str) -> str:
    color = input(mensaje)
    lista_colores = ["rojo", "azul", "amarillo", "verde", "rosa", "fucsia", "celeste", "marron", "negro"]
    validacion = validate_lista(color, mensaje_error, lista_colores)
    return validacion