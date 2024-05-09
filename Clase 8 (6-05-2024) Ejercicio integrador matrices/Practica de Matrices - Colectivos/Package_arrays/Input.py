from .Validate import *

def get_int (mensaje: str) -> int | None : 
    """_summary_: Recibe un string por parametro el cual evalua de que sea un 

    Args:
        numero (int): 

    Returns:
        int | None: retorna un numero de haber pasado la validacion.
    """
    numero = input(mensaje)
    validacion = validate_int(numero)
    return validacion


