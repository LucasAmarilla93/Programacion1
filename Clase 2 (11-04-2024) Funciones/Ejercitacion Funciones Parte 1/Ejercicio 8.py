# def potenciar (base, exponente) -> int:
#     acumulador_potencia = 0
#     match exponente: 
#         case 0 :
#             acumulador_potencia = 1
#         case 1 :
#             acumulador_potencia = base
#         case _:
#             for i in range (exponente - 1) :
#                 acumulador_potencia += acumulador_potencia * base
#     return acumulador_potencia


def potenciar (base: int, exponente: int) -> int: #Hacerlo con if
   potencia_realizada = base ** exponente
   return potencia_realizada

base_ingresada = input("Ingrese la base: ")
base_ingresada = int(base_ingresada)

exponente_ingresado = input("Ingrese el exponente: ")
exponente_ingresado = int(exponente_ingresado)

potencia = potenciar (base_ingresada,exponente_ingresado)
print(potencia)
