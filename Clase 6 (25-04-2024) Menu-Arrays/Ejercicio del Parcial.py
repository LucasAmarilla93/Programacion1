#Lucas Elias Amarilla   

#Desarrollar una función que reciba como parametros el precio de un producto, la cantidad y el porcentaje de descuento que se aplicara si la cantidad de productos supera las 10 unidades. La funcion retornara el precio de la compra con descuento (si corresponde)

def aplicar_descuentos(precio : int, cantidad: int, porcentaje_descuento: int) -> int | float :
    precio = precio * cantidad
    if cantidad > 10 :
        descuento = (precio * porcentaje_descuento) / 100 
        precio_final = precio - descuento
        precio = precio_final
        if precio_final < 0:
            precio = 0
    return precio

precio = int(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad del producto: "))
porcentaje_descuento = int(input ("Ingrese el descuento"))
descuento = aplicar_descuentos(precio, cantidad,porcentaje_descuento)
print(f"El precio final es de {descuento}$")