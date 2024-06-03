#Nombre y Apellido: Deben contener solo caracteres alfabéticos, ser nombres propios y no exceder los 20 caracteres. No pueden contener números ni caracteres especiales.
def validate_fullname (fullname: str, mensaje_error: str) -> str:
    while validate_sustantivo_propio(fullname) != True : #and fullname.isspace() == True and len(fullname) > 20 and (ord(fullname[1]) < 97):
        fullname = input(mensaje_error)
    return fullname

#Tengo que llamar a otras validate para numero. 

def validate_sustantivo_propio (cadena: str) -> bool:
    sustantivo_propio = False
    mayuscula = False
    minusculas = False
    for i in range(len(cadena)):
        if (ord(cadena[0]) > 65 and ord(cadena[0]) < 90):
            mayuscula = True
        else:
            if (ord(cadena[i]) > 97 and ord(cadena[i]) < 122):
                minusculas = True
    if mayuscula == True and minusculas == True:
        sustantivo_propio = True
    return sustantivo_propio


#Salario: Debe ser un valor numérico entero no menor a $234315.
def validate_salario (salario: int, mensaje_conversion: str, mensaje_error: str, minimo : int, max = 999999999) -> int | str:
    try:
        salario = int(salario)
    except:
        salario = input(mensaje_conversion)
        while salario.isnumeric () != True:
            salario = input (mensaje_conversion)
        salario = int(salario)

    while salario < minimo:
        salario = input(mensaje_error)
        salario = int(salario)
    return salario

#Puesto: Debe ser uno de los siguientes: “Gerente” / “Supervisor” / “Analista” / “Encargado” / “Asistente”.

def validate_puesto (puesto: str, mensaje_error: str) -> str:
    lista_puestos =["Gerente", "Supervisor", "Analista", "Encargado", "Asistente"]
    
    return puesto

#DNI: Debe ser un valor numérico entre 5000000 y 99999999.

def validate_dni (dni: int, mensaje_conversion: str, mensaje_error : str, minimo : int, maximo : int) -> str :
    try:
        dni = int(dni)
    except:
        dni = input(mensaje_conversion)
        while dni.isnumeric () != True:
            dni = input(mensaje_conversion)
        dni = int(dni)

    while dni < minimo or dni > maximo:
        dni = input(mensaje_error)
        dni = int(dni)
    
    return dni