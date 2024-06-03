#Nombre
#Genero
#Tecnologia
#Edad

def mostrar_trabajador(nombre, genero, tecnologia, edad) :
    print(f"{nombre}-{genero}-{tecnologia}-{edad}")

#Si yo quiero sacar o poner otro parametro me complicaria a nivel todas las funciones.

#Empezar a pensar los problemas en terminos de objetos. 
#Evitar el problema de escabilidad a la hora de programar. 

#Marco de ideas que sirve para encarar un proyecto de desarrollo de software.
#Se basa en definir objetos.
#Pienso el software como objetos de la vida real y como se relacionan dichos objetos.
#el paradigma orientada a objetos nos define la forma de producir codigo bajo ese paradigma. 

#############################Pilares del paradigma#################################################

"""
Abstraccion: Es la ignorancia selectiva. Puedo ver cosas del mundo real y empezar a clasificarlas: Estoy en la calle y veo un gato y un perro y se que ambas son animales. Si veo un poste de luz, se que no es un animal.
En el proceso de clasificacion podria definir las caracteristicas de un animal: ejemplo: la cantidad de patas, la forma de comunicacion, la forma de alimentarse, su cantidad de ojos, etc. 

Alumnos: altura de alumno o sueldo alumno en este marco universitario de la UTN por ejemplo no me interesa.
Ignoro lo que no me importa.

Encapsulamiento:
Protege la informacion de manipulaciones no autorizadas
#Ver video para completar a las 9.17

Polimorfismo:
Da la misma orden a varios objetos para que respondan de diferentes maneras

Todos los animales duermen, el perro duerme de la misma forma que un murcielago? Puedo decir que todos tienen la capacidad de dormir pero no todos implementan en el mismo algoritmo de dormir. 
Si tengo la posibilidad de mandar a dormir a todos los animales, lo haria, pero cada uno de los animales lo harian a su manera:
La accion es la misma, pero en el detalle cada uno lo hace a su manera. 

Herencia:
Las clases hijo heredan atributos y metodos de las clases padre.
Las mascotas que son animales, que pueden ser vertebrados o invertebrados y asi sucesivamente hasta llegar al concepto de animal hasta el punto de mascota.
Explotar un concepto generico hasta llegar a un concepto de animal generico. 

"""

##########################Objetos###############################################
"""
Objetos: Es una instancia de una clase

Una persona tiene caracteristicas (los cuales se denominan atributos, son las variables)
                                    : nombre, edad, direccion
                comportamientos(que se denominan COMPORTAMIENTOS)
                                : metodos (son las funciones en termino de programacion)
                                : correr, caminar, hablar, etc.


A las variables las llamamos atributos y a las funciones metodos.


Que es una clase: Se lo puede definir como un molde que definira las caracteristicas de un objeto y su comportamiento.

La clase define. Esta en un apartado abstracto, el objeto esta en el plano real.
La clase va a definir como va a ser el objeto.

"""

#Todo en python es un objeto.


""""

Pila                                                        Monton

                                            0x4788 Se reserva espacio en memoria

Se crea la variable con una id

                                            Se pasa el id al objeto.



mi_lista = lista()
        = []

"""

#VER VIDEO 9.47 PARA SABER BIEN LO DEL ESPACIO EN MEMORIA.