def validate_str(cadena: str, mensaje_error: str) -> bool:
    while cadena.isalpha() != True:
        #while (valor_caracter < 65 or valor_caracter > 90) and (valor_caracter < 96 or valor_caracter > 122) and valor_caracter != 32:
        cadena = input(mensaje_error)
    return cadena


def validate_int (numero: int, mensaje_error: str) -> bool:
    while numero.isdigit() != True:
        numero = input(mensaje_error)
    numero = int(numero)
    return numero 

def validate_lista (elemento: str, mensaje_error: str, lista: list) -> str:
    retorno = None
    while elemento not in lista:
        elemento = input(mensaje_error)
    retorno = elemento

    return retorno