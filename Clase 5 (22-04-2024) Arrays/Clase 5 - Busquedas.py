#Busquedas de cuentas, de banderas, de maximos y minimos.

lista = [45, 9, 300, -3, 100, -2 , 3]

#------------------------------------Busqueda de Calculos---------------------------------------------------#
suma = 0

#Quiero sumar los positivos

for i in range (len(lista)):
    if lista[i] > 0 : #por cada elemento de la lista, pregunto si ese elemento donde estoy parado es mayor a 0.
        suma = suma + lista [i]
        #tengo que iniciarlizar en 0 por afuera del scope para que se le asigne el valor a esta suma. 

print(f"La suma de los positivos es: {suma}")


#----------------------------------------MAXIMO-----------------------------------------------------#
bandera_maximo = True
maximo_numero = 0

for i in range (len(lista)):
    if bandera_maximo == True or lista[i] > maximo_numero : #Evaluo si es el primero (==True) o Los voy comparando ya.
        maximo_numero = lista[i]
        bandera_maximo = False

print(f"El maximo es: {maximo_numero}")

# maximo = max(lista) --->funcion que me da el maximo de la lista. 
# print(maximo)



#-----------------------------------Banderas------------------------------------------------------------#
#La bandera es un checkpoint, sirve para verificar si en el programa sucedio algo o no. 

#Quiero saber si hay un negativo, pero no me interesa contar.

bandera_negativo = False

#Necesito romper el algoritmo a penas encuentro el primer negativo. De esta manera sigue iterando TODOS LOS ELEMENTOS. Por eso tengo que cambiar el ESTADO DE LA BANDERA y ROMPERLO CON UN BREAK.
for i in range(len(lista)):
    if lista[i] < 0:
        bandera_negativo = True
        break

if bandera_negativo == True:
    print("Por lo menos hay un numero negativo")
else:
    print("No hay ningun numero negativo ") 


#----------------------------------------Buscar y Reemplazar----------------------------------------------------------#
numero_buscado = 3
reemplazo = 1000

for i in range(len(lista)):
    if lista[i] == numero_buscado:
        lista[i] = reemplazo #Me reemplaza todos los 3, ahora si quiero que reemplace solo 1, tendria que ponerle un break y salir. 

#-------------------------------------------------------------------------------------------------------------------#

#Que pasa si los pongo todo en funciones? Las listas se pueden parametrizar, se pueden pasar como parametro en una funcion y pueden ser devueltas tambien como una funcion.

#Una funcion puede recibir una lista, procesarla y devolver un True, un None, Un dict, lo que sea. 

#Parte de Control --> Si lo que entra a una funcion es realmente lo que estoy esperando. 
                    #Tengo que hacer cierto control y cacheo para ver que entra a la funcion.