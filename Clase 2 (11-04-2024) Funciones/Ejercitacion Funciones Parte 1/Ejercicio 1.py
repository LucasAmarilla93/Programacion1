#Nombre: Lucas Amarilla 

#Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def retornar_numero_entero ()  -> int :
    numero = input("Ingrese un numero entero: ")
    numero = int(numero)
    return numero

numero_entero = retornar_numero_entero()
print(f"Su numero es el: {numero_entero}")
#print(type(numero_entero))
