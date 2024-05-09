from os import system #Importar funciones de la consola.  #Funcion system del modulo os. 


def sumar_numero (un_numero, otro_numero) :
    suma = un_numero + otro_numero
    return suma



bandera_seguir = True
#Necesito indicar que tiene que ingresar numeros siempre. 
bandera_numeros_ingresados = False

#Primero tengo que mostrarle las opciones al usuario con un while infinito:
while bandera_seguir:
    opcion = input("1.Ingresar datos \n2.Sumar\n3.Restar\n4.Multiplicar\n5.Dividir\n6.Salir\nElija una opcion: ")
    opcion = int(opcion)
#Cuando sepa la opcion que quiera ejecutar el usuario, aca el programa deberia selicconar que accion va a realizar. 
    match opcion:
        case 1:
            #Plantear las funciones en cada caso. 
            print("Ingresando los numeros")
            numero_1 = int(input("Ingrese el primer numero: "))
            numero_2 = int(input("Ingrese el segundo numero: "))
            bandera_numeros_ingresados = True
        case 2:
            if bandera_numeros_ingresados == False:
                print("Primero debe ingresar los numeros")
            else:    
                resultado = sumar_numero (numero_1, numero_2)
                print("Sumando los numeros")
                print(f"El resultado de la suma es: {resultado}")
        case 3:
            print("Restando")
        case 4:
            print("Multiplicando")
        case 5:
            print("Dividiendo")
        case 6:
            seguir = input("Seguro que quiere salir")
            if seguir == "Si":
                bandera_seguir = False

#Esto esta fuera del match, dentro del while.
    system("pause") #Escribe una tecla para continuar.
    system("cls") #Borra la consola y vuelve a iterar. 