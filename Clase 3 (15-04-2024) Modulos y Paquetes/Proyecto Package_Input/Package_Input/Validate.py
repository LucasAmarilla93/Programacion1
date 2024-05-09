#validate_number() / validate_string ()

#Hago las validaciones de los numeros. 

def validate_number_int (numero: int, mensaje_error : str, minimo: int, maximo: int, reintentos: int) -> int | None:
    contador_reintentos = 0
    while numero < minimo or numero > maximo :
        if contador_reintentos != reintentos:
            numero = input(f"{mensaje_error}")
            numero = int(numero)
            contador_reintentos +=1
        else : 
            numero = None
            break

    return numero


def validate_number_float (numero: float, mensaje_error: str, minimo: float, maximo : float, reintentos: int) -> float | None:
    contador_reintentos = 0
    while numero < minimo or numero > maximo : 
        if contador_reintentos != reintentos :
            numero = input(f"{mensaje_error}")
            numero = float(numero)
            contador_reintentos +=1
        else :
            numero = None
            break
    return numero

def validate_string (cadena: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> str | None:
    cantidad_caracteres_cadena = len(cadena)
    contador_reintentos = 0
    while cantidad_caracteres_cadena < minimo or cantidad_caracteres_cadena > maximo :
        if contador_reintentos != reintentos : 
            cadena = input(f"{mensaje_error}")
            cantidad_caracteres_cadena = len(cadena)
            contador_reintentos += 1
        else :
            cadena = None
            break
    return cadena