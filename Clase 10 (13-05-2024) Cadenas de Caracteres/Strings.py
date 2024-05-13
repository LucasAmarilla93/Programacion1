#Puedo recorrer la cadena y acceder a cada uno de los elementos.

cadena = "Hola Mundo"
caracter = cadena [0]
#print(caracter)

#Repetir cadenas -> operador * (py)
#Slicing en python. 1:3

#Las cadenas son datos inmutables y no puedo cambiar su contenido.

#cadena [2] = "P" #--> tira una excepcion porque no soporta el string la asignacion de un item.

#####################################################SLICE####################################

#Es una caracteristica de Python. 

#Cortar la cadena dentro de una gran cadena que me pasan. 

#cadena = "Hola Mundo"
#print(cadena[5:10]) #Mundo. 

#subcadena = ""

#En lugar de usar el slice puedo utilizar un for para recorrerlo.

# for i in range(2, 6):
#     print(cadena[i], end= "")

# print(cadena[2:6])
# print(cadena[2:]) #Dos hasta el final
# print(cadena[:6]) #Del principio hasta el caracter 6
# print(cadena[0:]) #Principio hasta el final
# print(cadena[:]) #De principio hasta el final dicho de otra manera. 
# print(cadena[::-1]) #Lo recorre al revez. 

########################################Modificar letra de una cadena###############################################

cadena = "Hola Mundo"

cadena = "P" + cadena [1:]

print(cadena)

#Pero esto me crea una cadena nueva

#Se saca el largo con len y se concatena con el operador +

############################### Concatenacion #################################################################

cadena = "Hola mundo"
cadena_2 = ", como estan"
#cadena_3 = cadena + cadena_2
cadena_3 = f"{cadena}{cadena_2}"
print(cadena_3)


####################################### REPETICION ###################################################################

cadena = "Hola"

for i in range(3):
    print(cadena, end= "")

print("-" * 30) #Me imprime 30 veces lo mismo. 

####################################### Comparacion ###################################################

#Python compara por cada uno de los caracteres. Compara si una cadena esta por otra ordenada alfabeticamente. 


cadena = "hola"
print(cadena == "hola") #True
print(cadena != "hola") # False: porque son iguales
print(cadena == "Hola") # Cada letra tiene un valor en la tabla ASCII. No es lo mismo la "H" que la "h", la "H" vale menos que la otra
print(cadena > "Hola") # Me devuelve true porque la "h" vale mas que la "H"
print(cadena < "azul") # False, la a tiene un valor ASCII mas chico que la h de hola. 

##############Ordenar alfabeticamente una lista.#########################################################

nombres = ["Luis", "Beatriz", "Zaira", "Ana", "Jose"] 
                             # Si lo que esta aca es mas grande que lo que sigue, los intercambio.

for i in range(0, len(nombres) - 1):
    for j in range (i + 1, len(nombres)):
        if nombres [i] > nombres[j]: #Me ordena de la A a la Z, Chusmear bien esto.
            auxiliar = nombres [i]
            nombres [i] = nombres[j]
            nombres [j] = auxiliar
print(nombres)


############################################################################################################
#Cambiar de Mayuscula a miniscula.


cadena = "H3LA"

#Funcion ord para saber en python que ascii lleva. Pero es en algunos, es para saber el orden en la tabla Ascii.
cadena_2 = ""

#El problema de esto es que me va a sumar TODOS LOS CARACTERES. 
# for i in range (len(cadena)):
#     orden = ord(cadena[i]) + 32 #obtengo el orden.
#     caracter = chr(orden) #convierte entero a caracter.
#     cadena_2 += caracter

# print(cadena_2)
    
for i in range (len(cadena)):
    
    orden = ord(cadena[i])
    if orden >= 65 and orden <= 90:
        caracter = chr(orden + 32) 
        cadena_2 += caracter
    
    else:
        cadena_2 += cadena[i]

print(cadena_2)
    

#Otra forma
for i in range (len(cadena)):
    
    orden = ord(cadena[i])
    if orden >= 65 and orden <= 90:
        caracter = chr(orden + 32) 
        cadena_2 += caracter
        continue #Evitar que se sigan ejecutando las sentencias por del continue por debajo del for. La fuerza a la siguiente iterancion.
    
    cadena_2 += cadena[i]
    #Continue con el cadena_2 representa un IF. 

print(cadena_2)
    

#Otra forma --> gasta demasiados recursos pero sirve para buscar cosas. 

caracteres_validos = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

#Funcion que a partir de un caracter me diga si ese caracter es mayuscula.


#Deberia declarar una funcion y una bandera dentro de ella,
def es_caracter_valido(un_caracter, validos):
    es_valido = False
    for i in range (len(validos)):
        if un_caracter == validos[i]:
            es_valido = True
            break

    return es_valido


#Cuando hago una busqueda, cuando encuentro lo que estaba buscando lo rompo. Porque ya no hay necesidad de seguir buscando. 

cadena = "HoLa"





