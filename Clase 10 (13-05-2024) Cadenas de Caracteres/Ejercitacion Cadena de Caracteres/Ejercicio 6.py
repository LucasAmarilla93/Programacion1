#Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.

#Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.


def contar_subcadenas (cadena: str, subcadena: str) -> int:
    contador_subcadenas = 0
    #largo_subcadena = len(subcadena)
    #cadena_recortada = cadena[0:largo_subcadena]
    cadena_validacion = ""
    largo_subcadena = len(subcadena)

    #NO SE ESTA MOVIENDO. LLAMAR AL ORDENAMIENTO, una vez que lo encuentro, tengo que mover la I.
    for i in range (len(cadena)):
        cadena_validacion = cadena[i:largo_subcadena]
        largo_subcadena += 1
        if cadena_validacion == subcadena:
            contador_subcadenas += 1            
                
    return contador_subcadenas


#Partir en la cantidad de letras de la cadena?
#

subcadenas_contadas = contar_subcadenas("AACGTTTAATGTTCTAAGCTGCG", "CGTTTAATG")
print(subcadenas_contadas)


# cadena = "hola mundo"
# subcadena = "pan"
# subcadena_largo = len(subcadena)
# cadena_nueva= cadena[0:subcadena_largo]
# print(cadena_nueva)


#VER EN ONLINE GDB