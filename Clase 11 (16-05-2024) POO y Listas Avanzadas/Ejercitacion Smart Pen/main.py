from Class_boligrafo import * 
from Input import *
from Validate import *
from os import system

#Ojo de variables globales para leer y para escribir.

# boligrafo_dos = Boligrafo("grueso", "rojo")
# texto_escrito_dos = boligrafo_dos.escribir()
# print(texto_escrito_dos)


# cantidad_recargar = boligrafo_dos.recargar()
# print(cantidad_recargar)


def mostrar_menu ():
    opciones = input("""MENU DE OPCIONES:\nA.Escribir\nB.Recargar Lapicera\nc.Salir\nIngrese su opcion: """)
    return opciones

iterar = True
while iterar:
    opcion = mostrar_menu()
    match opcion:
        case "A":
            trazo = get_trazo("Ingrese el trazo: ", "Error en el trazo ingresado. Reingrese un trazo: ")
            color = get_color("Ingrese un color: ", "Error en el color. Reingrese un color:")
            boligrafo = Boligrafo(trazo, color)
            texto = boligrafo.escribir()
            print(texto)
        case "B":
            cantidad_recargada = boligrafo.recargar()
            print(cantidad_recargada)
        case "C":
            mensaje = input("¿Desea salir del menu?\nSi = y\nNo= n\nIngrese su opcion: ")
            if mensaje == "y":
                iterar = False
    
    system("pause")
    system("cls")

