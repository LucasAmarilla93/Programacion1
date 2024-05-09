#Nombre: Lucas Amarilla

#Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.

#Dentro del concepto de reutilizables existe la posibilidad de llamar funciones desde otros ejercicios. 

dato_ingresado = input("Ingrese un dato:") #Todo lo que ingreso aca me lo devuelve como string. Entonces tengo que preguntarlo en la funcion es un digito. 

def ingresar_numero_entero (dato) -> int : #Yo deberia tomar el dato y ver si se puede transformar a int. 
    while dato.isdigit() == True:
        numero_entero = dato
        return numero_entero

def ingresar_numero_flotante (dato) -> float : 
    while dato.isdecimal() == True:
        numero_flotante = dato
        return numero_flotante

def ingresar_cadena (dato) ->str :
    while dato.isascii() == True:
        cadena = dato
        return cadena


numero_int = ingresar_numero_entero(dato_ingresado)
numero_float = ingresar_numero_flotante(dato_ingresado)
cadenda_ingresada = ingresar_cadena (dato_ingresado)

print (f"El numero entero es: {numero_int}")
print (f"El numero flotante es: {numero_float}")
print (f"La cadena es: {cadenda_ingresada}")

string = "Hola"
string.isalnum()
string.isdigit()
string.isnumeric()
string.isascii()
string.isalpha()
string.isdecimal()