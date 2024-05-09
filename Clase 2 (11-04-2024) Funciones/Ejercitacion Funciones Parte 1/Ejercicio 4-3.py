dato_ingresado = input("Ingrese una cadena: ")

def ingresar_cadena (dato:str) -> str:
    while dato.isalpha() != True:
        dato= input("Reingrese una cadena: ")
    return dato

cadena = ingresar_cadena(dato_ingresado)

print(f"Su cadena es la siguiente: {cadena}")
    