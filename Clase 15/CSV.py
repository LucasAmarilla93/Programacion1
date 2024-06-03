#Archivo de texto que respeta un formato en donde yo puedo interpretar el dato por filas, separando por cada fila los datos que quiero guardar por comas y puntos y comas. 
#CSV: commas separated values. 
#Lineas de texto donde cada dato esta separado por un delimitador : ","

#Nombre, apellido y edad de 3 personas.
#puedo hacer una lista de objetos, un diccionario o una lista paralela.

nombres = ["Juan","Maria","Luis"]
apellidos = ["Lopez", "Gomez", "Ruiz"]
edades = [20,35,42]

#Listas paralelas: Cada componente se corresponde con la componente omonima de la otra lista. Es decir Juan Lopez 20 años es un entidad.

#Puedo crear el registro y guardarlo.

#O puedo:
with open("agenda.csv", "w") as archivo:
    for i in range(len(nombres)): #por cada dato que tenga en la lista.
        linea = f"{nombres[i]},{apellidos[i]},{edades[i]}\n"
        archivo.write(linea) 

#######################################################################
#para no escribirlo todo el tiempo hago lo siguiente, donde me lo escribe sola una vez y no por cada iteracion.


linea = ""
for i in range(len(nombres)): #por cada dato que tenga en la lista.
    linea += f"{nombres[i]},{apellidos[i]},{edades[i]}\n"

with open("agenda.csv", "w") as archivo:
    archivo.write(linea)


#########################################################################

with open("agenda.csv", "r") as archivo:
    for linea in archivo: #quiero cortar esta cadena en pedacitos
        registro = linea.split(",")
        print(registro) #Sigo teniendo el mismo problema con el \n
        print(f"{registro[0]} -- {registro[1]} -- {registro[2]}")


#Como le saco el registro [2] le saco el \n puedo hacer replace, strip pero es un relaburo. 

############################ EXPRESIONES REGULARES #################################################
#Conjunto de caracteres que nos sirven de patron de busqueda. 
#Tecnicas para manipular strings. 

#En este caso debo establecer un doble criterio de corte. 

#Tengo que importar el modulo re(regular expression)

import re

with open("agenda.csv", "r") as archivo:
    for linea in archivo: #quiero cortar esta cadena en pedacitos
        registro = re.split(",|\n", linea) #es mas inteligente que el otro split, me permite que le pase mas de un criterio de corte. 
        print(registro)
        print(f"{registro[0]} -- {registro[1]} -- {registro[2]}")
        #me deja un elemento vacio, el registro 2 esta libre de \n.