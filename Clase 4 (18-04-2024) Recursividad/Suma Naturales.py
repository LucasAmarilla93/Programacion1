def calculcar_suma_naturales (numero: int) -> int:
    if numero == 0 : #buscar caso base. 
        resultado = 0
    else :
        resultado = numero + calculcar_suma_naturales(numero - 1)
    
    return resultado


calculo = calculcar_suma_naturales(4)
print(calculo)