from Package_Input.Input import *

dato_int = get_int ("Ingrese un numero: ", "Error. Reingrese un numero: ", 1, 10, 3 )
print(dato_int)

dato_float = get_float ("Ingrese un flotante: ", "Error. Reingrese un flotante: ", 1.25, 5.99, 3)
print(dato_float)

dato_str = get_string ("Ingrese una cadena: ", "Error. Reingrese otra cadena: ", 1 , 10 , 3)
print(dato_str)
