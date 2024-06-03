#QUEVEDO || BZRP Music Sessions #52,827192970,204,https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg,https://youtube.com/watch?v=A_g3lMcWVy0,2022-07-06 00:00:00


import re


def parser_csv (path: str) -> list: #REGLA GENERAL: SI LA FUNCION DEVUELVE LIST; LA CREO Y RETORNO.
    lista = []

    with open(path, "r", encoding = "utf8") as archivo:
        #recorro cada linea del archivo y creo un registro.
        for linea in archivo:
            registro = re.split(",|\n", linea)
            diccionario = {}
            diccionario["titulo"] = registro [0]
            diccionario["vistas"] = registro[1]
            diccionario["duracion"] = registro[2]
            diccionario["url"] = registro[4]
            lista.append(diccionario)

    return lista



#print(lista_temas)

#Hay caracteres raros como por ejemplo en Khea con el corazon, entonces al momento de leer se rompe., le tengo que decir al open con que tipo de codificacion va a trabajar.
#por eso paso el enconding con utf8

#ENCODING es el sistema de codificacion que necesita el archivo para poder leer o escribir caracteres especiales.

#escribir en un archivo csv los datos que yo pase.
def generar_csv(path: str, lista: list): #Puede tener todos los temas o algunos temas nomas. 
    with open(path, "w", encoding= "utf8") as archivo:
        for tema in lista:
            linea = f"{tema["titulo"]},{tema['vistas']},{tema['duracion']},{tema['url']}\n"
            archivo.write(linea)

#Grabo la lista en el archivo.

lista_temas = parser_csv("Clase 15\data.csv")

for tema in lista_temas:
    print(f"{tema["titulo"]}")

otra_lista = [lista_temas[0], lista_temas[1], lista_temas[2], lista_temas[3]]

generar_csv("copia.csv", otra_lista)