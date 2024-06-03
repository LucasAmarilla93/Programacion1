#Metodos de Strings

#############################################Strip ################################################

#Eliminara los caracteres vacios (por default) que pueda contener la variable. 
cadena = "            hola mundo               "
cadena = cadena.strip()
cadena = cadena + "div 111"
print(cadena)

#Por default, borra los que estan a la derecha y a la izquierda.

cadena_dos = "°°°°°°°°Hola mundo°°°°°°°°°"
cadena_dos = cadena_dos.strip("°")
print(cadena_dos)

cadena.lstrip() #borra a la izquierda
cadena.rstrip() #borra a la derecha


####################################### Upper y Lower ##############################################
#Transforma la cadena a todo mayuscula o a todo minuscula

cadena = cadena.upper()
print(f"La cadena en mayuscula: {cadena}")

cadena = cadena.lower()
print(f"La cadena en minuscula: {cadena}")


####################################### Capitalize ###################################################
#Pone la primer letra en mayuscula. 

cadena = cadena.capitalize() #Pone solo el primer caracter en mayuscula. 
print(cadena)
cadena = cadena.title() #Pone el primer caracter de cada palabra en mayuscula. 
print(cadena)

###################################### Replace ########################################################
#Reemplazara un conjunto de caracteres por otro.

cadena_reemplazada = cadena.replace ("la", "--")
print(cadena_reemplazada)

####################################### Split ########################################################

#Divide una cadena en cadenas subpequeñas.
#Divide, separa y aquello que separa devuele una lista de strings. 
#Necesito el caracter delimitador -> aquel caracter que toma para dividir. 
cadena_spliteada = "Java,Python,C#,C"
lenguajes = cadena_spliteada.split(",")
print(lenguajes)
print(type(lenguajes)) #List
lenguajes = cadena_spliteada.split("C") #["Java,Python," , "#," , ""]

#Expresiones regulares -> Investigar. 

######################################## Join ######################################################
#Puedo concatenar cadenas a traves de un delimitador. 
#Siempre recibe algo que se pueda iterar.

delimitador = ","
lista_lenguajes = ["Java", "Python", "C#", "C"]
cadena_lenguajes = delimitador.join(lista_lenguajes)
print(cadena_lenguajes)

######################################### zfill ######################################################

numero = 5
print(f"{numero :05}") #Se hace sobre el formato del string. 

numero_dos = "222"
cadena_z = numero_dos.zfill(6) #cuantos digitos quiero que autocomplete con 0 -> Se hace sobre el string.
print(cadena_z)


######################################## isalpha #######################################################
#Devuelve TRUE si todos los caracteres son alfabeticos (de la A a la Z)

cadena = "hola"
print(cadena.isalpha())

cadena = "hola mundo" #el espacio no es un caracter valido.
print(cadena.isalpha())

cadena = "hola mundo 123"
print(cadena.isalnum()) #False por el espacio nuevamente. 

cadena = "holamundo123"
print(cadena.isalnum())

######################################## count ############################################################
#Cuenta la cantidad de incidencias de una cadena con una subcadena especifica

cadena = "hola mundo hola mundo"
cantidad = cadena.count("la")
print(cantidad)

####################################### find ###############################################
#Muestra solamente la primera vez que encuentra la palabra mundo. 

indice = cadena.find("mundo") #Me devuelve 5 porque es ahi donde esta indexado mundo
print(indice)

indice = cadena.find("mundo", 10) #Buscar a partir del caracter 10

print(indice)



#CUANDO UN METODO NO NECESITA DE LA INSTANCIA SE DENOMINA METODO ESTATICO. 