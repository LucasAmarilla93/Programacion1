import json

def parser_json(path: str) -> list:
    #list = [] #esta vez no voy appendeando cosas a la lista.

    with open(path, "r") as archivo:    
        diccionario = json.load(archivo) #me devuelve un diccionario.

    return diccionario["bzrp"]

mi_lista = parser_json("Clase 15\data.json") #ya queda deseralizado.
print(mi_lista)



def generar_json(path: str, lista: list): #ojo porque es un diccionario, pero representa la lista de cosas que quiero escribir.
    with open(path,"w") as archivo:
        json.dump(lista, archivo, indent = 4)


otra_lista = [mi_lista[0], mi_lista[1], mi_lista[2], mi_lista[3]]

#Tiene que estar dentro de un diccionario para serializarla.

diccionario = {}
diccionario["bzrp"] = otra_lista #la misma clave para que sea consistente.

generar_json("copia en json", diccionario)