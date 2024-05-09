#Lucas ELias Amarilla


#Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente reemplazo y luego retornar la cantidad total de reemplazos realizados.

def reemplazar_nombres(lista: list, nombre: str, reemplazo: str) -> int :
    contador_reemplazos = -2
    if type(lista) is list:
        contador_reemplazos = -3
        if len(lista) > 0 :
            contador_reemplazos = 0
            for i in range (len(lista)):
                if lista[i] == nombre :
                    lista[i] = reemplazo
                    contador_reemplazos += 1

    return contador_reemplazos

lista = ["martin", "Lucas", "Vanesa", "Julian"]

reemplazo_nombres = reemplazar_nombres(lista, "martin", "Reemplazo")
if reemplazo_nombres == -2 :
    mensaje = "Ingrese un dato del tipo LISTA"
elif reemplazo_nombres == -3 :
    mensaje = "La lista esta VACIA"
elif reemplazo_nombres == 1 :
    mensaje = f"Se realizo {reemplazo_nombres} reemplazo"
else :
    mensaje = f"Se realizaron {reemplazo_nombres} reemplazos"
print(mensaje)