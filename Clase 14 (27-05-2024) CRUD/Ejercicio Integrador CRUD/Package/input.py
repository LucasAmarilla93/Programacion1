from validate import *

def get_str_fullname (mensaje: str, mensaje_error: str) -> str :
    cadena = input(mensaje)
    validacion = validate_fullname(cadena, mensaje_error)
    return validacion

def get_str_puesto (mensaje: str, mensaje_error: str) -> str:
    cadena = input(mensaje)
    cadena = validate_puesto(cadena, mensaje_error)
    return cadena

def get_int_salario (mensaje: str, mensaje_conversion: str, mensaje_error: str, minimo: int) -> int:
    numero = input(mensaje)
    numero = validate_salario(numero, mensaje_conversion, mensaje_error, minimo)
    return numero

def get_int_dni (mensaje: str, mensaje_conversion: str, mensaje_error: str, minimo: int, maximo: int) ->int:
    numero = input(mensaje)
    numero = validate_dni(numero, mensaje_conversion, mensaje_error, minimo, maximo)
    return numero


nombre =  get_str_fullname("Ingrese su nombre: ", "Reingrese un nombre valido: ")

#salario = get_int_salario("Ingrese su salario", "error de conversion", "error salario", 10000)

#puesto = get_str_puesto("Ingrese su puesto", "Puesto no encontrado")

#dni = get_int_dni("Ingrese su dni", "Erro de conversion", "error", 0, 50000)