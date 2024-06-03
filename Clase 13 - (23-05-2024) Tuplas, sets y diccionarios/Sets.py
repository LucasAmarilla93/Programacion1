############################### SET #####################################
#Coleccion de elementos con la particularidad de que no contiene elementos duplicados.
#No respetan el orden en el que fueron declarados.
#Sus elementos son mutables.

#Set se crea a partir de una lista. Las listas las puedo convertir a tupla y a set o viceversa.

mi_set = {5,6,7,5,5,5,9,8,1,9,-6} #Creo un set con llave.

#Pensar el set como conjunto. 
print(mi_set) #no respeto el orden de los elementos declarados, tampoco los ordeno de menor o mayor. 

#Puedo acceder a elementos particulares. 


#como no es una lista, tengo que recorrerlo.

for elemento in mi_set:
    print(elemento)

#Es MUTABLE.

#################################### ADD ############################################################
#Como el append o insert.

mi_set.add(100)
print(mi_set) #lo insertó donde quiso.

################################### Remove ############################################################

mi_set.remove(9)
print(mi_set)

#Si le paso algo que no existe al remove, me tira una EXCEPCION. NO ES SEGURO.
#Investigar MANEJO DE EXCEPCIONES. 

#Para trabajarlo de manera segura utilizo un DISCARD.

mi_set.discard(5)
print(mi_set)
#Si le paso un valor que no existe, no elimina nada pero tampoco se rompe el programa. 

elemento = mi_set.pop() #elimina el elemento del indice 0
print(elemento)
elemento = mi_set.pop() #elimina el elemento del indice 0 SIEMPRE // Comportamiento de Pila. 
print(elemento)

###################################### CLear ################################################################

mi_set.clear()
print(mi_set)

################################### Operaciones entre conjuntos #############################################

#Podriamos hacer una union, interseccion o diferencia. 
#AUB
set_a = {3,4,5} #instancia de un set
set_b = {6,2,3} #otra instancia de un set

union = set_a.union(set_b) #Metodo de instancia. Llamo al metodo union a traves de una instancia.
#REPASAR METODOS DE INSTANCIA Y DE CLASE. 

#set.union(set_a,set_b) #metodo de clase.  --> INVESTIGAR.

print(union) #Si hay algo que se repite no lo tengo en cuenta. Como en los conjuntos.

########################################## INTERSECCION ######################################
#Elemento que se repite en los dos
#AnB

interseccion = set_a.intersection(set_b)
print(interseccion) 

########################################## Diferencia #########################################################
#A-B de los conjuntos. 

diferencia = set_a.difference(set_b) #Valores de A que no estan en B.
print(diferencia)

diferencia_dos = set_b.difference(set_a) #Valores de B que no estan en A.

