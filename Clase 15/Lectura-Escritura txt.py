#escritura de texto

archivo = open("mi_primer_archivo.txt","w") #El nombre del archivo tambien debe incluir la ruta donde voy a trabajar el archivo. 
#Si yo pongo solo el nombre, lo va a crear o leer al directorio raiz de la app.

#Escribo el archivo. 
archivo.write("Hola mundo") #esto sobreescribe y va creando el archivo nuevamente. 
#el archivo permanece abierto hasta que lo cierre.
archivo.close() #Si yo quiero escribir o algo despues de esto no puedo porque ya me lo cerró.

#archivo.write("AGREGO ALGO") #me tira excepcion.

print(archivo.closed)

##########################################################################################################################

archivo = open("mi_primer_archivo.txt", "a") #modo append, lo adjunta. 
archivo.write("\n Como estan DIV 111")
archivo.close()


#Aprender como absolutizar rutas. 


#####################################################################################################################
archivo = open(r"C:\Users\lucas\Desktop\UTN\UTN PRIMER CUATRIMESTRE\Programacion 1\mi_primer_archivo.txt","r") #absolutizar la ruta.
contenido = archivo.read() #agarrra y  lee todo el archivo y devuelve un str con todo lo que pudo leer.
print(contenido)
archivo.close()


#asi nome lo encuentra. 
#La ruta de los archivos se escriben con doble barra o la contrabarra.
#si el archivo esta en un directorio totalmente distinto al directorio raiz de la app, hago click derecho en el archivo y cambio el path directorio

#archivo = open(r"Carpeta\mi_primer_archivo.txt", "r") 

###################################################################################################################

lista = ["Gio", "Mati", "Ale", "Gianni"] #Escribir la lista en un archivo.
archivo = open("nombre.txt", "w") 
#archivo.write(lista) #no me lo corre porque el argumento tiene que ser un str, no una list.
#tengo que convertir la lista en texto: recorrer la lista, concatenar los archivos a variable y escribirla o:

for nombre in lista: #por cada nombre en la lista. -> Nombre es del tipo lista. 
    archivo.write(f"{nombre}\n") #Me devuelve GioMatiAleGianni uno al lado del otro si no le doy algun tipo de formato.
    #Lo que yo le pase me lo va a escribir como texto.
archivo.close()

#Con el for escribo 4 veces en el archivo, una por cada cadena. 

##############################################################################################################
archivo = open("nombre2.txt", "w")
archivo.writelines(lista) #un iterable con lineas, pero me lo junta. y me devuelve GioMatiAleGianni.
archivo.close()

############################# Mejor opcion ##################################################################

cadena = ""
for nombre in lista: 
    cadena += f"{nombre}\n"

archivo = open("nombre.txt", "w")
archivo.write(cadena)
archivo.close()


#El acceso a disco es mucho mas costoso que el acceso a memoria. 


######################### Administrador de contexto #########################################################
#Crea un recurso y cuando termina de usarlo lo libera.
#Ej. crear una coneccion de base de datos y el mismo administrador se encarga de cerrarlo, lo mismo con un txt o con un objeto y cuando termina el bloque lo pasa al garbage collector.

with open("nombre.txt", "r") as archivo:  
    #por default si no pasa nada el modo default es lectura
    #open devuelve un objeto, pero voy a decir que el open sea como archivo.
    #puedo empezar a usar el archivo.

    #Metodo readlines.
    contenido = archivo.readlines() #devuelve una lista de str para leerlo
    #me trae el salto de linea desde el archivo tambien. 

print(contenido)

for nombre in contenido:
    print(nombre.upper(), end="") #Ya tiene dentro un salto de linea. #Aparecen de manera inconsistente. Lo soluciono a nivel visual unicamente. 
    print(len(nombre)) #porque me toma el \n



##############################################################################################################
#El objeto file es iterable. 

with open("nombre.txt", "r") as archivo: #Hace lo mismo de arriba. ITERO DIRECTAMENTE EL ARCHIVO.
    for linea in archivo:
        print(linea) #en cada iteracion me devuelve por cada lectura un string.
        #no fue necesario hacer un read.



##########################################################################################################

try:  #intento ejecutar el codigo que es suceptible a una excepcncion.
    with open("nombres.txt", "r") as archivo: #Hace lo mismo de arriba. ITERO DIRECTAMENTE EL ARCHIVO.
        for linea in archivo:
            print(linea)
except: #que hago en el caso de que haya una excepncion.
    print("El archivo no existe")