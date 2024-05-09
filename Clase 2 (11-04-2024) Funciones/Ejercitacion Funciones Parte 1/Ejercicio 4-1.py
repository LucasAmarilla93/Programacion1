dato_ingresado = input("Ingrese un entero:") #Todo lo que ingreso aca me lo devuelve como string. Entonces tengo que preguntarlo en la funcion es un digito. 

def ingresar_numero_entero (dato:int) -> int : #Yo deberia tomar el dato y ver si se puede transformar a int. 
    while dato.isdigit() != True: 
        dato = input("Reingrese un dato: ")
    dato = int(dato)
   # print(type(dato))
    return dato

numero_int = ingresar_numero_entero(dato_ingresado)

print (f"El numero entero es: {numero_int}")