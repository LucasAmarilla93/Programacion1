#Nombre: Lucas Amarilla

#Crear una función que le solicite al usuario el ingreso de una cadena y la retorna. 

def ingresar_cadena () -> str :
    cadena = input("Ingrese una cadena: ")
    cadena = str(cadena)
    return cadena

cadena_ingresada = ingresar_cadena()
print(f"Su cadena es la siguiente: {cadena_ingresada}")
#print(type(cadena_ingresada))