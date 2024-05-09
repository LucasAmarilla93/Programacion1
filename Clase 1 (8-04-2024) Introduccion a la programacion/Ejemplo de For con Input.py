acumulador = 0

for i in range (5) :
    numero = input ("Ingrese un numero: ")
    numero = int(numero)
    acumulador += numero
    #acumulador = acumulador + numero

promedio = acumulador / (i + 1)

print(f"El promedio es : {promedio} y la suma es: {acumulador}")
#print("El promedio es {0} y la suma es {1}".format (promedio,acumulador))