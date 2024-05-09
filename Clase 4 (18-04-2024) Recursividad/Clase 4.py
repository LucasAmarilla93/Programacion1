#Quiero mostrar un mensaje 10 veces.

# for i in range (10):
#     print("hola")

#Lo quiero definir recursivamente. 

def cuenta_regresiva (iteraciones: int) -> int : 
    if iteraciones != -1: #esto se va a ejecutar hasta que llegue a 0
        print(iteraciones)
        #puedo hacer iteraciones -= 1
        cuenta_regresiva(iteraciones - 1)
        #En algun momento yo tengo que volver a llamar a la funcion, tengo que pasarle un conjunto de datos mas chicos    para que trabaje con eso.

#hice algo repetitivo sin usar repeticiones. 
#Es similar a uns mamushka. 


# for i in range (10, -1, 1): #Exactamente igual a la recursividad.
#     print(i)

#Si no puedo resolver algo de manera iterativa o si tengo que usarlo de manera iterativa pero me quedo un choclo, entonces tengo que llamar a la recursion. 

#Si yo pongo el numero 1000. Fue recursion de 996 veces y se llego al maximo de recursion en memoria. 
#Llame a la funcion tantas veces que se apilo de mas en la memoria y la sature. -->RecuirsionError: maximum recursion depth exceeded. --> Se genero un overflowing

#Para probar esto se utiliza el calculo el factorial sirve para hacer combinaciones y permutaciones. 
    #"De cuantas formas distintas puedo yo usar el color rojo, verde y azul"
    #Factorial = es el n multiplicado por ese numero - 1, siempre y cuando el numero sea mayor a 0


numero = 5
factorial = 1 #Tiene que valer 1 porque sino en el bucle for siempre va a iterar por 0 
for i in range(1, numero + 1) : #i toma valores desde el uno hasta el 5. 
    factorial *= i #Recordar el tema de los cauntificadores. 
    
    print(factorial)

"""
Detras de escena. 
numero = 5
factorial = 1

i=1
factorial = 1 * 1 = 1
i= 2
factorial = 1 * 2 = 2
i= 3 
factorial = 1 * 2 * 3 = 6
i = 4
factorial = 1 * 2 * 3 * 4 = 24
i = 5
factorial = 24 * 5 = 120
"""

#---------------------------------------------------------------------------------------------------------#

def calcular_factorial(numero: int) -> int : #Tengo que definir mi caso base o limite.
    if numero == 0: #caso base.  Con esto va a salir de la recursividad. 
        resultado =  1
    else: 
        resultado = numero * calcular_factorial (numero - 1)
    
    return resultado

numero = 4
factorial = calcular_factorial(numero)
print(f"El factorial de {numero} es: {factorial}")

#Las llamadas a funciones se van a ir apilando. En el stack de memoria.

#En el stack de memoria se cargan las llamadas a funciones y las variables en memoria. Es una parte de la ram que se designa. 

"""
stack de memoria  ----→ es eficaz pero no eficiente (cada llamada a funcion, requiere mas memoria, llama mas instancias, etc) Tengo 2 creaciones de variables, una evaluacion, una cuenta, otra cuenta otra asignacion a las cuentas y son un monton de movimientos en memoria!!!. 

me da 1
calculcar_factorial(0)
calcular_factorial(1)
calcular_factorial(2)
calcular_factorial(3)
calcular_factorial(4)
calcular_factorial(5)
"""
#Python como no es tipado, ataja lo que venga.  Permite hasta 999 en este caso. 

