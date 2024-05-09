#Nombre: Lucas Amarilla 

#Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def ingresar_numero_flotante () -> float :
    numero = input("Ingrese un numero flotante: ")
    numero = float(numero)
    return numero

numero_flotante = ingresar_numero_flotante()
print(f"Su numero es: {numero_flotante}")
#print(type(numero_flotante))