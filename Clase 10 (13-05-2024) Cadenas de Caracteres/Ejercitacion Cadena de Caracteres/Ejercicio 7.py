def encontrar_subcadena (lista: list, subcadena: str) -> str | None:
    cadena_validacion = ""
    mensaje = "Son todos inocentes"
    nombre = ""
    #voy a recorrer la lista y dentro evaluo.
    for i in range(len(lista)): #cada elemento de la lista.
        largo_subcadena = len(subcadena)
        # yo no quiero que me haga esto en los nombres.

        for j in range(len(lista[i])): #accedo a cada base nitrogenada
            cadena_validacion = lista[i][j:largo_subcadena]
            print(cadena_validacion)
            largo_subcadena += 1
            
            if cadena_validacion == subcadena:
                mensaje = f"Se encuentra culpabe a: {lista[i - 1]}"

    
    return mensaje


lista_sospechosos = ["Juan Perez","CGGGGCTAAAATTTTTTACGATCG", "Maria Rodriguez", "AACGTTTAATGTTCTAAGCTGCG", "Carlos Sanchez", "CGGGGCTAAAATTTTTTACGATCG"]

sospechoso = encontrar_subcadena(lista_sospechosos, "CGTTTAATG")
print(sospechoso)
    

""""
     nombre Maria   Juan    Julian   
base        xcs      xcs     xcs 



"""