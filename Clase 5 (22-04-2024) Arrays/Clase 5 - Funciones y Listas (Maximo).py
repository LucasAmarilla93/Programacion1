def buscar_maximo(lista: list) -> int: 
    bandera_maximo = True
    for i in range (len(lista)):
        if bandera_maximo == True or lista[i] > maximo_numero: 
            maximo_numero = lista[i]
            bandera_maximo = False
    
    return maximo_numero

lista = [44, -9, 77]

maximo = buscar_maximo(lista)
print(f"El valor maximo es: {maximo}")