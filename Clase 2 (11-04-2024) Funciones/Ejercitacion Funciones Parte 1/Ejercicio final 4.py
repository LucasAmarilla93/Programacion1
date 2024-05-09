def ingresar_numero_entero (dato:int) -> int : 
    while dato.isdigit() != True: 
        dato = input("Reingrese un dato: ")
    dato = int(dato)
    return dato

def ingresar_numero_flotante (dato:float) -> float : 
    while dato.isdecimal() != True :
        dato = input ("Reingrese un numero flotante: ")
    dato = float(dato)
    return dato

def ingresar_cadena (dato:str) -> str:
    while dato.isalpha() != True:
        dato= input("Reingrese una cadena: ")
    return dato

dato_ingresado_entero = input("Ingrese un entero:")
dato_ingresado_flotante = input ("Ingrese un flotante: ")
dato_ingresado_cadena = input("Ingrese una cadena: ")


numero_float = ingresar_numero_flotante(dato_ingresado_entero)
numero_int = ingresar_numero_entero(dato_ingresado_flotante)
cadena = ingresar_cadena(dato_ingresado_cadena)

print (f"El numero entero es: {numero_int}")
print (f"El numero flotante es: {numero_float}")
print(f"La cadena es la siguiente: {cadena}")
    