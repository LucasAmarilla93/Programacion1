#get_int() / get_float() / get_string()

#aca llamo a las funciones de validar desde el modulo de VALIDATE para usarlas. 

from Validate import *
#Importo todo de validate. 


#Validate unicamente me valida lo que ingreso, y lo devuelve. ahora tendria que pasarle a validate los parametros que deseo ingresar.
def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    number = input(mensaje)
    number = int(number)
    validacion = validate_number_int(number, mensaje_error, minimo, maximo, reintentos)
    return validacion

#dato = get_int ()
#print(dato)

def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float| None:
    numero_flotante = input(mensaje)
    numero_flotante = float(numero_flotante)
    validacion_flotante = validate_number_float(numero_flotante, mensaje_error, minimo, maximo, reintentos)
    return validacion_flotante

#dato_flotante = get_float("Ingrese un flotante: ", "Error. Reingrese un flotante: ", 1.25, 9.99, 3)
#print(dato_flotante)

def get_string(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> str | None:
    cadena = input(mensaje)
    validacion_cadena = validate_string(cadena, mensaje_error, minimo, maximo, reintentos)
    return validacion_cadena

# dato_cadena = get_string("Ingrese una cadena: ", "Error. Reingrese otra cadena: ", 1, 10, 3)
# print(dato_cadena)


ejemplo = get_int ("Hola", "hola", 1,2,3)
print(ejemplo)