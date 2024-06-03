"Como a traves de metodos, podemos manipular las listas"

lista = [5,9,7]

print(type(lista))
#La lista es un objeto, dentro de la clase lista
print(lista)
########################### Append ################################################
#Genera un elemento mas al final de la lista.

lista.append(1) #genera un espacio mas en memoria para agregar un entero mas a la lista.
lista.append("Perro")
lista.append([5,9,7])
print(lista)

######################### Insert #########################################################
#el insert mete un elemento en un indice especificado.
#corre los elementos a la derecha desde el indice donde yo especifique. 


lista.insert(2, 10)
print(lista)

#El metodo prevee que el indice que yo le paso es mayor al len(lista), hace como un append, el insert llama al append.

############################# Vaciar lista ################################################

#FOR EACH -> for elemento in lista.

for _ in range(len(lista)): #No necesitaba la variable de control en este caso.
    lista.pop(0) #elimina el tope, desde el primer plato.

print(lista)

for elemento in lista: #Por cada elemento que tengo en la lista, guarda todos los numeros. #PARA CADA ELEMENTO QUE ESTA EN LA LISTA: 
    if elemento == 9 :
        lista.remove(elemento)
print(lista)

cont = 0
while cont < len(lista):
    if lista[cont] == 9 or list[cont - 1] == 9:
        lista.remove(9)
    cont += 1

############################## Remove ################################################
#Itera la lista, busca el match con el elemento y donde lo encuentra lo elimina.

lista_dos = [5,9,7,8,9,9,9]

lista.remove(9)
print(lista_dos)

############################ pop ######################################################
#elemento de que posicion quiero sacar y me devuelve el elemento.

elemento = lista.pop(2)
print(elemento)
print(lista)

################################# index ##############################################
#Devuelve el indice.


################################ sort##################################################
#ordena la lista de menor a mayor.

lista.sort() #ordena de menor a mayor. 
print(lista)

lista.sort(reverse = True) #me devuelve los elementos ordenados al revez. 

################################## Reverse ##############################################
#dar vuelta el vector.
lista.reverse() #da vuelta el vector


############################### Clear ###############################################
lista.clear()
#Limpia la lista, no deja de existir pero se vacio.

##############################  DEL #############################################
#Es un destructor
del(lista) #Pasa al garbage colector, borra la instancia de memoria. 



