def buscar_reemplazar(lista: list, busqueda: int, reemplazo: int) -> bool : #Hago verificaciones y si devuelve True o false segun el caso sea.
    retorno = False
    if type(lista) is list and type(busqueda) == int and type(reemplazo) is int:
        retorno = True
        for i in range(len(lista)):
            if lista[i] == busqueda:
                lista[i] = reemplazo
                break #rompo porque lo cambio. 
    return retorno

#Esta funcion unicamente modifica la lista por eso no tiene un retorno. 

lista = [44, -9, 77]

if buscar_reemplazar(lista, 44, 1000):
    for i in range (len(lista)):
        print(lista[i])
else:
    print("Hubo un error. No pasaste una lista")


#Quiero que reemplace todas las incidencias de este valor. 
def buscar_reemplazar_dos(lista: list, busqueda: int, reemplazo: int) -> bool : #Hago verificaciones y si devuelve True o false segun el caso sea.
    retorno = False
    if type(lista) is list and type(busqueda) == int and type(reemplazo) is int:
        retorno = True
        for i in range(len(lista)):
            if lista[i] == busqueda:
                lista[i] = reemplazo 
    return retorno



#Si quiero que esta funcion haga una cosa o la otra. Que reemplace el primer numero encontrado o todos los numeros encontrados del mismo valor. 
def buscar_reemplazar_tres(lista: list, busqueda: int, reemplazo: int, reemplazo_todo: bool) -> bool : #Hago verificaciones y si devuelve True o false segun el caso sea.
    retorno = False
    if type(lista) is list and type(busqueda) == int and type(reemplazo) is int:
        retorno = True
        for i in range(len(lista)):
            if lista[i] == busqueda:
                lista[i] = reemplazo 
                if not reemplazo_todo : #if reemplazo_todo == False:
                    break
    return retorno