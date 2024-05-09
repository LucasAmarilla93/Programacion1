def buscar_negativo(lista: list) -> bool: 
    bandera_negativo = False
    for i in range(len(lista)):
        if lista[i] < 0:
            bandera_negativo = True
            break
    return bandera_negativo
lista = [44, -9, 77]


if buscar_negativo(lista):
    print("Por lo menos hay un numero negativo")
else:
    print("No hay ningun numero negativo ") 
