"""
Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente). La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.
Por ej:
cadena = “murcielaguito”

“a” 1
“e” 1
“i” 2
“o” 1
“u” 2  
"""

def determinar_vocales (cadena: str) -> int | None: 
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0
    
    for i in range (len(cadena)):
        orden = ord(cadena[i])      
        match orden:
            case 97 | 65:
                contador_a += 1
            case 101 | 69:
                contador_e += 1
            case 105 | 73:
                contador_i += 1
            case 111 | 79:
                contador_o += 1
            case 117 | 85:
                contador_u += 1 
    
    mensaje = f"A: {contador_a}\nE: {contador_e}\nI: {contador_i}\nO: {contador_o}\nU: {contador_u}"

    return mensaje


vocales = determinar_vocales("Algarrobo")
print(vocales)