#Lucas Elias Amarilla. 

#Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def encontrar_maximo (primero:int, segundo: int, tercero: int) -> int :
    if primero > segundo and primero > tercero :
        numero_maximo = primero
    elif segundo > tercero :
        numero_maximo = segundo 
    else :
        numero_maximo = tercero 
    return numero_maximo
    
    
primer_numero = input("Ingrese un numero: ")
primer_numero = int(primer_numero)
segundo_numero = input ("Ingrese un segundo numero: ")
segundo_numero = int (segundo_numero)
tercer_numero = input ("Ingrese un ultimo numero: ")
tercer_numero = int(tercer_numero)

maximo = encontrar_maximo(primer_numero,segundo_numero,tercer_numero)

print(f"El numero maximo es: {maximo}")




