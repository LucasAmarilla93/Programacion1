#Importar los paquetes desde otro proyecto. 

#Carga secuencial.

mi_lista = [0] * 5 #Inicializo todos los datos en 0.
#Puedo iniciarlo con lo que quiera, con un false, un string, un true, lo que yo guste representando un VALOR ILOGICO. 
#Aca la lista tiene valores ya cargados con los que puedo trabajar. 
#Si quiero tomar el valor 0, tengo que inicializar en FALSE para poder cargar el 0

#mi_lista = [] #->pierdo las caracteristicas de usarlo de otra forma. La lista esta vacia y estoy obligado a cargar un elemento con un metodo.


#Agregar datos a la lista.
for i in range (len(mi_lista)):
    mi_lista [i] = int(input("Ingrese un numero: ")) #---> Puedo pedir que ingrese el dato que yo quiero y los va a ir acomodando en los distintos indices. Puedo utilizar funciones como get_int, get_string. 


#Printear la lista.
for i in range (len(mi_lista)):
    print(mi_lista[i])

#---------------------------------------------------------------------------------------------------------#

#Carga aleatoria: Cargar de manera Random o lo que el usuario requiera la lista o el verctor. 

mi_lista_dos = [-1] * 5 #lo inicializo en un valor ilogico. Es un valor que indica que ahi no hay nada, y tendria que filtrarlo cuando los muestro. Muestro todo menos los que tengan -1 como valor.

bandera_salida = True

#No quiero hacer una carga total del vector, uso un while. 
while bandera_salida == True:
    index = int(input("Ingrese una posicion: "))
#Tengo que hacer una validacion porque si me ingresa una posicion mas grande, me rompe el programa. 

    while index < 1 or index > len(mi_lista):
        index = int(input("Ingrese una posicion: "))

    numero = int(input("Ingrese un numero: "))

    mi_lista [index - 1] = numero  #Tengo que indicar en que posicion de la lista voy a guardar y eso me lo va a dar index. 
    #Mi lista en la posicion index me ingresas el numero donde que yo ingreso.
    #En el index siempre hay que ver donde va, porque para el usuario si quiere guardar en el 1, yo voy a guardar en la 2 posicion, entonces tengo que restarle al index - 1 por un tema de cuentas. 
    #El usuario carga donde quiera, pero yo tengo que mantener la coherencia de los indices. 

    seguir = input("Continuar? si/no")
    if seguir == "no":
        bandera_salida = False



#Otra forma 
# while True: -->bucle infinito. 
#     index = int(input("Ingrese una posicion: "))
#     numero = int(input("Ingrese un numero: "))

#     mi_lista [index] = numero  #Tengo que indicar en que posicion de la lista voy a guardar y eso me lo va a dar index. 
#     #Mi lista en la posicion index me ingresas el numero donde que yo ingreso.

#     seguir = input("Continuar? si/no")
#     if seguir == "no":
#         break -->lo uso para romper el bucle infinito. 


#Procedimientos separados. 

for i in range (len(mi_lista)):
    print(mi_lista[i])

#Si pongo en la posicon  99, el valor 1 -> me tira un out of range. 

for i in range(len(mi_lista)):
    if mi_lista[i] != -1:
        print(f"Indice: {i + 1} / Valor ingresado: {mi_lista[i]}")

