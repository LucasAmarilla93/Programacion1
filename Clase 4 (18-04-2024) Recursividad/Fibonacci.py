def calcular_fibonacci (numero: int) -> int:
    if numero == 0 or numero == 1:
        resultado = numero    
    else:
        resultado = calcular_fibonacci (numero - 1) + calcular_fibonacci (numero - 2) 
    
    return resultado

calculo = calcular_fibonacci(2)

print(calculo)


"""
                             1        0
                     F(2) = F(1) + F (0) --> 1
                        1      1
               F(3) = F(2) + F (1) / --> 1 + 1
                2  +   1 
       F(4) = F(3) + F (2) 
        3         
F(5) = F(4) + F(3)
                \
                 F(3) = F(2) + F(1)
                        F(2) = F(1) + F(0)



"""