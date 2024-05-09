
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
    """_summary_: Valida si el numero ingresado esta en la lista de legajos.

    Args:
        numero (int): Numero ingresado a comparar con el legajo.
        legajo (list): Legajo donde se encuentran los numeros que dan continuidad a la funcion

    Returns:
        bool: True en caso de coincidir los numeros, False en caso de no haberlo hallado.
    """
    retorno = False
    if numero != None:
        for i in range (len(legajo)):
            if legajo[i] == numero:
                retorno = True
    return retorno
#Tengo que validar el numero en una funcion aparte. Si lo hago todo junto se me rompe todo el codigo porque la iteracion no me devuelve nada


def validar_reintentos_chofer (numero: int ,legajo: list, reintentos = 3 ) -> str | int:
    """_summary_ Valida la cantidad de reintentos que el usuario puede ejecutar al ingresas el legajo.

    Args:
        numero (int): Recibe el numero de legajo
        legajo (list): Lista donde se encuentran los legajos admitidos
        reintentos (int, optional): Cantidad de reintentos posibles

    Returns:
        str: Devuelve el mensaje de error y corta la ejecucion si se superan los intentos
        int: Devuelve el numero de legajo ya validado.
    """
    contador_reintentos = 0 
    
    while validar_legajo_chofer(numero, legajo) == False:
        if contador_reintentos != reintentos:
            numero = input("Error. Reingrese un legajo existente: ")
            numero = int(numero)
            contador_reintentos += 1
        else :
            numero = "Se han superado todos los intentos posibles."
            print(numero)
            break
    
    return numero

def validar_rango (mensaje: str, numero: int, min: int, max: int) -> int:
    """_summary_: Valida el rango permitido.

    Args:
        mensaje (str): Dependiendo del coche o linea, sera uno u otro.
        numero (int): El valor a comparar con los minimos y maximos.
        min (int): El valor minimo permitido.
        max (int): El valor maximo permitido.

    Returns:
        int: _description_
    """
    while numero < min or numero > max: 
        numero = input(mensaje)
        numero = int(numero)

    return numero