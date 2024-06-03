##################################### TUPLAS #################################################

#Similares a las list, con la particularidad de ser INMUTABLES -> No se puede modificar el valor, elementos o largo de la misma.

tupla = tuple([5,6,4]) #->constructor y le paso los elementos.
print(type(tupla))
print(tupla) #-> no tiene corchetes, sino que tiene parentesis. |

#Puedo crear una tupla a traves de parentesis.
tupla_dos = (5,7,[0,7,8])

#Se acceden como los elementos de una lista.
print(tupla_dos[0]) #me da pauta de que es algo iterable.

for elemento in tupla:
    print(elemento)

####### No puedo modificar los elementos de la tupla ##########

#tupla[1] = 5 #tuple object does not support item assignment 

#Pero si un elemento de una tupla fuera una lista, cambia la cosa

tupla_dos[2][0] = 250

print(tupla_dos) #Se modifico el elemento porque tengo una referencia como el elemento array. Me abstraigo de la tupla y modifico un tipo de dato inmutable. Se modifico un elemento de algo de la tupla que si es mutable. 

#Crear una tupla vacia NO TIENE SENTIDO!!!
#tupla =()

tupla_tres = (5) #No es tupla, sino es un entero
#Python entiende que este elemento es un valor unico que si a la tupla le asigno otra cosa de iguales caracteristicas va a seguir siendo entero. 

tupla_cuatro = (4,) #-> me toma como una tupla de un solo elemento
print(len(tupla_cuatro)) #unica constante.

##################### Tupla para representar color ############################
NEGRO = (0,0,0)

#Cuando necesito que un dato no cambie, lo represento como tupla.

################### Las tuplas se pueden desempaquetar ##########################

tupla_cinco = (4,9,6)
#a = tupla_cinco[0]
#b = tupla_cinco[1]
#c = tupla_cinco[2]

#DESEMPAQUETADO
a,b,c = tupla_cinco  #a,b y c van a ser iguales a la tupla. El = desempaqueta los valores de manera ordenada de la tupla.

#a la funcion le llega la tupla y luego la desempaqueto. 


####################### METODOS DE CONSULTA #############################################

tuple_seis = (4,9,6,4)
print(tuple_seis.count(4)) #saber la cantidad que hay
print(tuple_seis.index(9)) #saber el index del valor. 

