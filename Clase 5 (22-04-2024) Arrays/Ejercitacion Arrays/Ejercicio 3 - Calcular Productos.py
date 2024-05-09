#Lucas Elias Amarilla

#Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

def calcular_producto_numeros(lista: list) -> int :
    producto = False
    if type(lista) is list:
        producto = True
        if len(lista) > 0 :
            for i in range (len(lista)):
                producto *= lista[i]
    return producto

lista = [3, 5, 10, 25]
producto_lista = calcular_producto_numeros(lista)

if producto_lista == False :
    mensaje = "Ingrese un dato de valor lista"
elif producto_lista == True :
    mensaje = "La lista ingresada esta vacia"
else :
    mensaje = f"El producto de la lista es: {producto_lista}"

print(mensaje) 