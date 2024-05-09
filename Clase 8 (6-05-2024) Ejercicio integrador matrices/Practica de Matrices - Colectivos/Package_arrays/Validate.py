def validate_int(numero: int) -> int:
    """_summary_: Evalua si el input recibe un dato del tipo int.
    Args:
        numero : int
    Returns:
        int: me devuelve el entero de haber pasado la validacion. 
    """
    while numero.isdigit() != True:
        numero = input("Reingrese un dato del tipo numero: ")
    numero = int(numero)
    return numero

def validar_legajo_chofer (numero: int, legajo: list) -> bool:
    retorno = False
    if numero != None:
        for i in range (len(legajo)):
            if legajo[i] == numero:
                retorno = True
    return retorno
#Tengo que validar el numero en una funcion aparte. Si lo hago todo junto se me rompe todo el codigo porque la iteracion no me devuelve nada


def validar_reintentos_chofer (numero: int ,legajo: list, reintentos = 3 ) -> str:
    contador_reintentos = 0 
    
    while validar_legajo_chofer(numero, legajo) == False:
        if contador_reintentos != reintentos:
            numero = input("Error. Reingrese un legajo existente: ")
            numero = int(numero)
            contador_reintentos += 1
        else :
            numero = "Se han superado todos los intentos posibles."
            break
    
    return numero

def validar_rango (mensaje: str, numero: int, min: int, max: int) -> int:
    while numero < min or numero > max: 
        numero = input(mensaje)
        numero = int(numero)
        
    return numero
