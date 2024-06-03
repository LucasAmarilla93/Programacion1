#Crear una función que reciba como parámetro una cadena y determine si la misma es o no un palíndromo. Deberá retornar un valor booleano indicando lo sucedido.

def determinar_palindromo (cadena: str) -> bool:
    palindromo_estado = False
    cadena_palindromo = ""
    cadena_minuscula = ""

    #Transformo la cadena entera a minuscula para su evaluacion.
    for j in range(len(cadena)):
        if ord(cadena[j]) > 64 and ord(cadena[j]) < 91: #si la primera es mayor, la convierto a menor.
            letra_minuscula = ord(cadena[j]) + 32
            letra_minuscula = chr(letra_minuscula)
            cadena_minuscula += letra_minuscula
        else:
            cadena_minuscula += cadena[j]

    for i in range (len(cadena_minuscula) - 1, -1, -1): #Recordar que el index no me lo evalua la ultima.
        cadena_palindromo += cadena_minuscula[i]

    if cadena_minuscula == cadena_palindromo:
        palindromo_estado = True
    
    return palindromo_estado


palindromo = determinar_palindromo("Kayak")
print(palindromo)


#Ana
#Anna
#Otto
# 0 1 2
# A N A

# 2 1 0
# A N A

#Comparo si las dos anas son iguales.