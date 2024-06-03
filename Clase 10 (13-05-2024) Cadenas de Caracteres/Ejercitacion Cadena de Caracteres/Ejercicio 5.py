#Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.
#Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.


def eliminar_vocales (cadena: str) -> str:
    cadena_nueva = ""
    for i in range(len(cadena)):
        letra = ord(cadena[i]) #le hago el order a cada letra.
        if letra != 97 and letra != 65 and letra != 101 and letra != 69 and letra != 105 and letra != 73 and letra != 111 and letra != 79 and letra != 117 and letra != 85:
            cadena_nueva += cadena[i]

    return cadena_nueva


cadena_sin_vocales = eliminar_vocales("vocaleeeeeeeeeeeeeeeeees")
print(cadena_sin_vocales)