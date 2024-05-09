#Hay dos controles con una lista: el relacionado al tipo de dato y otra al contenido o cantidad de elementos de esa lista..

#La lista puede recibir cualquiera cosa. 

#-----------------------------------------------TIPO DE DATO---------------------------------------------#

def sumar_positivos(lista: list) -> int | float | bool | None: #sumar los numeros positivos. 
    retorno = False #La funcion devuelve no porque lo de abajo no se cumple. 
   # if type(lista) is list and len(lista) > 0: 
        #Me devuelve el tipo de dato que esta entrando. "Si esto es una lista" (type == lista)
        #Tengo que hacer el control ahora para saber si hay POR LO MENOS UNO.

        #El and de un if se vuelve un IF ANIDADO:
    if type(lista) == list:
        retorno = True
        if len(lista) > 0:
            retorno = 0 #/--->inicializa el retorno y lo carga. 
            for i in range(len(lista)):
                if lista[i] > 0:
                    retorno += lista[i]

       #retorno = 0 
       #Tengo que declarar la variable suma (retorno). LA FUNCION VA A DEVOLVER 0 SIEMPRE Y CUANDO YO INGRESE UNA LISTA SIEMPRE Y CUANDO RECIBA UNA LISTA Y TENGA UN ELEMENTO.
    
    #Cuando la funcion verifica y sabe que hay un elemento mas, recien ahi la funcion retorna 0 y ejecuta 
    #    for i in range(len(lista)):
    #        if lista[i] > 0:
    #            retorno += lista[i]

    return retorno

lista = [44]
#lista = [45, 9, 300, 3, 100, 2, 3]

suma = sumar_positivos(lista)
if suma == None:
    print("El valor ingresado no es una lista") #-->Hay que especializarlo un poco
elif  suma == True:
    print("La lista esta vacia")
else :
    print(suma)

#--------------------------------------------CONTENIDO-------------------------------------------------------#.

#Aca es la misma funcion pero ejecutada con otros tipos de codigo porque no uso EL TIPO DE DATO sino un VALOR EN SI. 
def sumar_positivos(lista: list) -> int | float | bool | None:
    """_summary_ "DOCUMENTAR FUNCIONES SI O SI"

    Args:
        lista (list): _description_

    Returns:
        int: [-2: NO RECIBE UNA LISTA][-1: SI LA LISTA ESTA VACIA][> = 0: SI PUDO CALCULAR LA SUMA.]
    """
    #sumar los numeros positivos. 
    retorno = -2
    if type(lista) == list:
        retorno = -1
        if len(lista) > 0:
            retorno = 0 #/--->inicializa el retorno y lo carga. 
            for i in range(len(lista)):
                if lista[i] > 0:
                    retorno += lista[i]
    return retorno

if suma == -2:
    print("El valor ingresado no es una lista") #-->Hay que especializarlo un poco
elif  suma == -1:
    print("La lista esta vacia")
else :
    print(f"La suma de los positivos es: {suma}")

