def sumar_digitos (numero: int) -> int:  
   
   # if numero > 10 : #Si el numero es mas grande, necesito dos operaciones, una para sacar el decimal de ese numero y otra para sacar el modulo de ese numero. 
        #3245 / 10 --> 324.5 --> es nuevamente mayor a 10? SI --> / 10 --> 32.45 -> same --> 3.245 Es un float, me quedo solo con la parte entera.  LO CASTEO Y COMO ES MENOR A 10 me guarda el 3. --| int(3.245)  -> 3
        
        #3245 % 10 --> Me devuelve el 5 y es el ultimo numero y me lo guardo. OJO ACA

        #Saque el numero mas grande que es el 3 y el 5 que es el ultimo.

        #Faltan 2 y 4.
        #324.5 % 10 --> 4.5
        #32.45 % 10 --> 2.45

    if numero < 10 : 
        resultado = numero #tengo que castearlo a int. porque seria el ultimo de los divididos y me resultaria en un flotante. --> Caso base.     
    else :
        resultado = sumar_digitos(numero / 10) + numero % 10 #aca va guardando los restos en cada recursion.
        resultado = int(resultado)
    return resultado


sumar = sumar_digitos(125)
print(sumar)

"""
Como condicion 

¿Cuando yo corto la ejecucion?

SI YO TENGO UN SOLO DIGITO ENTONCES LO DEVUELVO. ES EL CASO MAS CHICO Y LO SUMO. ME RERESENTA EL CASO BASE.

45 // 10 = 4 --> entero -->el numero es mayor a 10, por ende tengo dos digitos y para sacar el segundo tengo que hacer el modulo.

45 % 10 = 5 --> entero  
            ---> cada vez que es mayor a 10 tengo que hacer el modulo tambien para sacar el segundo digito.


459 //10 = 45 // 10 = 4,5 --> apila todo, me devuelve el 4 -->aca se convirtio en un FLOAT.

           45 %  10 = 5 ---> apila todo, me devuelve el 5
*---> falta encontrar el 5 ---> EL 5 aparece una vez que le hago el modulo a 45 *

459 % 9 --> el ultimo de la pila que me devuelve. 

"""

