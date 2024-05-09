dato_ingresado = input("Ingrese un flotante:") #Todo lo que ingreso aca me lo devuelve como string. Entonces tengo que preguntarlo en la funcion es un digito. 
#Validarlo en rango a todos entonces. 
#Validarlo era como validarlo en tipo. 

def ingresar_numero_flotante (dato:float) -> float : 
    while dato.isdecimal() != True :
        dato = input ("Reingrese un numero flotante: ")
    dato = float(dato)
    return dato

numero_float = ingresar_numero_flotante(dato_ingresado)

print (f"El numero flotante es: {numero_float}")
