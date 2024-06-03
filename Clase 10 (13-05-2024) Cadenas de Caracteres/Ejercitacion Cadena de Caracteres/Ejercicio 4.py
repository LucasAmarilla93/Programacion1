#Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos.
#	Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.

#Debe eliminar solamente los repetidos, no todos. 


def suprimir_caracteres_repetidos (cadena: str) -> str:
    cadena_nueva = ""
    for i in range(len(cadena)):
        if i == (len(cadena) - 1): #si es el anteultimo directamente lo sumo, sino, voy evaluando.
            cadena_nueva += cadena[i]
        else:            
            if cadena[i] != cadena[i+1]: #si son distintos, los sumo, sino no.
                cadena_nueva += cadena[i]

    return cadena_nueva
#cadena = suprimir_caracteres_repetidos("hoooooola")
#print(cadena)

cadena = suprimir_caracteres_repetidos("comooooo vaaaaa ??????")
print(cadena)