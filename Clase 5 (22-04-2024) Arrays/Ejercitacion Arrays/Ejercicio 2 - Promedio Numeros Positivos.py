#Lucas Elias Amarilla

#Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
def promediar_numeros_positivos(lista: list) -> int | float :
    promedio = False
    if type(lista) is list :
        promedio = True
        if len(lista) > 0 :
            suma_promedio = 0
            for i in range (len(lista)):
                if lista[i] > 0:
                    suma_promedio += lista[i]
            promedio = round(suma_promedio / len(lista), 2)
    return promedio    

lista = [12, 25, 33]
promedio_lista_positivos = promediar_numeros_positivos(lista)

if promedio_lista_positivos == False:
    mensaje = f"Inserte un dato del tipo lista"
elif promedio_lista_positivos == True:
    mensaje = f"Ingresó una lista vacia"
else: 
    mensaje = f"El promedio de los positivos es: {promedio_lista_positivos}"

print(mensaje)