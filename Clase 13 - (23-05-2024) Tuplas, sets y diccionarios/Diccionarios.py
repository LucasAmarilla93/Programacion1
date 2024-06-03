#Pensamos un diccionario como un diccionario del colegio. 
#Tenemos una palabra clave y para esa palabra una definicion.
#Voy a tener una o mas claves (key) y para cada una voy a tener un valor asociado (value)

diccionario = {
    'nombre'  : 'Luis', #la key puede ser un string, un numero, puede ser cualquier cosa.
    'edad' : 19, #el value puede ser un string, un int, un obj, una tupla, un set, otro diccionario, etc.
    'ciudad' : 'Cordona',
}

#Para acceder al diccionario, lo pienso como en forma de lista, pero accedo al Value a traves de la Key. No estan indexados. 
#Pensamos en diccionario como lista pero con los key. 

print(diccionario['nombre'])
print(diccionario['edad']) #me piso la edad de 19.
#print(diccionario["EDAD"]) # me tira una excepcion porque no existe.

#print(diccionario['edad']) #me imprime la ultima. 

#Los diccionarios son dinamicos.
#Puedo agregar una clave por fuera del diccionario:

diccionario["profesion"] = "estudiante"
print(diccionario["profesion"])

edad = diccionario.pop("edad")
print(edad)
print(diccionario)

print(diccionario.keys()) #me devuelve toda las claves del diccionario en una lista.
print(diccionario.values()) #me devuelve una lista con todos los valores
print(diccionario.items()) #me devuelve una lista de tuplas, en donde cada elemento de la tupla representa una clave y un valor.

#recorro el diccionario

for clave in diccionario: #por cada clave en el diccionario, imprimo la clave.  #por default diccionario devuelve las claves.
    print(clave)


for clave in diccionario.keys(): #la palabra clave dentro del for obtiene CADA UNA DE LAS CLAVES. En la iteracion muestro el valor de una clave distinta.
    print(diccionario[clave])
    #obtener valor por esa clave.

#Desempaquetar cada item.

for clave, valor in diccionario.items(): #cada item devuelve una tupla, el elemento [0] va a clave y el elemento [1] va a valor.
    print(f"{clave} -> {valor}")


#SENTIDO DEL DICCIONARIO Y DEL OBJETO.

#Objeto siguen el modelo de entidad. Sirven para representar una entidad compleja que tiene atributos y metodos.(comportamiento y estado) -> Respetan los pilares de la POO. Esta enfocado para representar un modelo de datos: si represento los datos de una facultad: alumnos, profesores, materias, mesas de examen. 
#Podria tener como atributo un diccionario.
#Tendria sentido tener una clase para representar el domicilio? con Altura, calle, codigo postal? Quizas no tiene sentido crear una clase, pero si dentro de un objeto puedo tener un diccionario que represente el domicilio. 

#los diccionarios los utilizamos cuando tengo que representar un dato que no tenga peso por si misma, que no sea una entidad, configurar parametros, para datos dinamicos o para serializar y deserializar cosas de un archivo o hacia un archivo. 
#si hago una pagina web y necesito los datos para poder conectarme:
    config = {
      "host" : "localhost",
      "port" : 8080,
      "debug" : True
   }
    
#sirven para las configuraciones iniciales.
#puedo guardar la configuracion inicial de un usuario al loggearse a una aplicacion. 
#archivos j.son estructura particular de datos bastante estandarizada. Se usa en varios lenguajes de programacion. Un json es json para cualquier lenguaje, de muchisima utilidad. 