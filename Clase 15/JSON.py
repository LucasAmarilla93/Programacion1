#los archivos json son archivos universales. Son tan standar que sirven para trabajar en la mayoria de los lenguajes de programacion.
#Viene de JavaScript Object Notation
#Sirve para el intercambio de datos basado en texto. 

#hay que importa el metodo json
import json

#se parece a un diccionario, al momento de guardar los datos deberiamos tener algo parecido a eso.

diccionario1 = {"nombre" : "Juan", "edad" : 25 }
diccionario2 = {"nombre" : "Maria", "edad" : 30 }
diccionario3 = {"nombre" : "Luis", "edad" : 39 }

lista = [diccionario1, diccionario2, diccionario3]
#el metodo dump no entiende lo que es una lista. 
#voy a tener que crear un diccionario para guardar esto. 

data = {} #data es igual a un diccionario.

data["personas"] = lista  # la lista es un valor para una clave dentro de un diccionario mas grande.

with open("personas.json", "w") as archivo:
    json.dump(data, archivo, indent= 4) #me pide los datos y el archivo.
 #indent estructura el archivo.

lista_personas = data["personas"]
print(lista_personas[0])



with open("personas.json", "w") as archivo:
    json.load(archivo)

lista_personas = data["personas"]

print(lista_personas[0])