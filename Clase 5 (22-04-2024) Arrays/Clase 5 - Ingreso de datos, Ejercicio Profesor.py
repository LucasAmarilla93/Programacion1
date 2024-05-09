def mostrar_lista(lista: list, vacio: int) -> bool:
    retorno = False
    if type(lista) is list and len(lista) != 0 and type(vacio) is int:
        retorno = True
        for i in range(len(lista)):
            if lista[i] != vacio:
                print(lista[i])
    
    return retorno

def verificar_lugar(lista: list, posicion: int, vacio: int) -> bool|None:
    retorno = None
    if type(lista) is list and type(posicion) is int and type(vacio) is int:
        retorno = False 
        if lista[posicion] == vacio:
            retorno = True
    return retorno 

def responder_salida(mensaje: str) -> bool:
    seguir = input("Queres ingresar otro? si/no: ")
    if seguir == "si":
        bandera_seguir = True
    else:
        bandera_seguir = False

    return bandera_seguir



def cargar_lista(lista: list) -> bool:
    bandera_seguir = True

    while bandera_seguir == True:
        posicion = int(input("Posicion: "))
        while posicion < 1 or posicion > len(lista):
            posicion = int(input("Reingrese posicion: "))
        
        if verificar_lugar(lista, posicion-1, -1):
            numero = int(input("Ingrese un numero: "))
            lista[posicion - 1] = numero
        else:
            print("La posición ya esta ocupada")

        bandera_seguir = responder_salida("Desea continuar ingresando?")



mi_lista = [-1] * 5

cargar_lista(mi_lista)

if not mostrar_lista(mi_lista, -1):
    print("Hubo algun error")