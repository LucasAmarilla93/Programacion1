def crear_empleado(id: int, nombre: str, apellido: str, dni: int, puesto: str, salario: int) -> dict: 
    diccionarios_empleado = {
        "ID" : id,
        "nombre" : nombre,
        "apellido" : apellido,
        "dni": dni,
        "puesto" : puesto,
        "salario" : salario
    }

    return diccionarios_empleado

