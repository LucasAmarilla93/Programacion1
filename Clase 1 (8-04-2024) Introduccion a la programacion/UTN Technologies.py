'''
UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, que promete revolucionar el mercado.

Las posibles aplicaciones son las siguientes:
Inteligencia artificial (IA),
Realidad virtual/aumentada (RV/RA),
Internet de las cosas (IOT)

Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

A) Los datos a ingresar por cada empleado encuestado son:
nombre del empleado
edad (no menor a 18)
género (Masculino - Femenino - Otro)
tecnologia (IA, RV/RA, IOT)  

B) Cargar por terminal 10 encuestas.

C) Determinar:
Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.

Nombre: Lucas Elias Amarilla
'''

cantidad_masculinos_tecnologia = 0
cantidad_empleados_iot_rvra = 0
cantidad_total_empleados = 0 
nombre_masculino_mayor_edad = ""
tecnologia_masculino_mayor_edad = 0 
edad_mayor_masculino = 0
bandera = True

for i in range (10):
    nombre = input ("Ingrese el nombre: ")
    
    edad = input ("Ingrese la edad: ")
    edad = int(edad)
    while edad < 18 :
        edad = input ("Ingrese nuevamente la edad: ")
        edad = int(edad)
        

    genero = input ("Ingrese el genero (Masculino, Femenino u Otro) :  ")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input ("Ingrese nuevamente el genero: ")

    tecnologia = input ("Ingrese la tecnologia (IA, RV/RA, IOT): ")
    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        tecnologia = input ("Ingrese la tecnologia: ")

#Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
    match genero :
        case "Masculino":
            match tecnologia:
                case "IA"  | "IOT":
                    if edad > 24 and edad < 51:
                        cantidad_masculinos_tecnologia += 1
            if bandera == True :
                edad_mayor_masculino = edad
                nombre_masculino_mayor_edad = nombre
                tecnologia_masculino_mayor_edad = tecnologia
                bandera = False
            else:
                if edad > edad_mayor_masculino :
                    edad_mayor_masculino = edad
                    nombre_masculino_mayor_edad = nombre
                    tecnologia_masculino_mayor_edad = tecnologia
        
    match tecnologia :
        case "IOT" | "RV/RA":
            match genero : 
                case "Masculino" | "Otro" :
                    if edad < 33 or edad > 40 :
                        cantidad_empleados_iot_rvra += 1
                    
    cantidad_total_empleados = i + 1

#Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
#SIEMPRE HAY QUE REALIZAR LAS VALIDACIONES POR 0 en PROMEDIOS y PORCENTAJES. 
if cantidad_empleados_iot_rvra != 0 : 
    porcentaje_empleados_iot_rvra = (cantidad_empleados_iot_rvra * 100) / cantidad_total_empleados
else :
    porcentaje_empleados_iot_rvra = 0

#Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.
print (f"La cantidad de masculinos con IA / IOT es : {cantidad_masculinos_tecnologia}, el porcentaje es: {porcentaje_empleados_iot_rvra}\n El nombre de la persona es : {nombre_masculino_mayor_edad} y la tecnologia es {tecnologia_masculino_mayor_edad}")
