from class_personaje import Personaje

#Creo un personaje. Llama al constructor.
Personaje_1 = Personaje("IronMan",True,True,"Tener plata", 500)
personaje_2 = Personaje ("Thor", False, True, "Trueno", 700)


print(id(Personaje_1))
print(type(Personaje_1))
print(f"{Personaje_1.nombre}") #desde el punto de vista de la clase, self es IronMan en este caso. Si tuviese otro, seria otra cosa.
    #Operador.nombre para acceder a casi "todo" dentro de la clase.

#print(f"{Personaje_1.nombre} - {Personaje_1.poder_pelea} - {Personaje_1.super_poder}")


def mostrar_personaje (un_personaje: Personaje):
    #Puedo agregar, cambiar, caracteristicas, pero el prototipo def mostrar_personaje. etc no cambia.
    print(f"{un_personaje.nombre} - {un_personaje.poder_pelea} - {un_personaje.super_poder}")


#Ya no llamo a una funcion que me describa al personaje. Directamente le pido al personaje que se describa. Tiene sentido que el mismo objeto se describa a si mismo. Una accion que lleva a cabo el objeto.
#mostrar_personaje(Personaje_1)
#Personaje_1.describirse() #Ahora tengo una funcion que se describe. Le pido a personaje_1 que se describa.
#mostrar_personaje(personaje_2)
#personaje_2.describirse()

print(Personaje_1.describirse())
print(personaje_2.describirse())


###########################################################################################################
personaje_3 = Personaje("SpiderMan", True, False, "Muerte Instantanea", 300)


descripcion = Personaje_1.describirse()
print(descripcion)

Personaje_1.volar(1000, 200)


personaje_3.volar(100,50) #Spiderman intenta volar pero no lo deja.

personaje_3.puede_volar = True #Le cambian el traje permitiendole volar.

personaje_3.volar(100,50) #SpiderMan vuela a esa altura y velocidad.


#El enemigo no sabe que ironman puede volar, solo sabe que puede volar, entonces eso es ENCAPSULAMIENTO.


##################################################################################################################

personaje_2.atacar(Personaje_1)

Personaje_1.atacar(personaje_3) #Tiene mas poder de pelea que Spiderman

personaje_4 = Personaje("Groot", False, False, "Ramas", 500)

Personaje_1.atacar(personaje_4)

######################################################################################################################

print(Personaje_1.describirse())
print(personaje_2.describirse())
print(personaje_3.describirse())
print(personaje_4.describirse())

######################################################################################################################
lista_heroes :list[Personaje]= [] #Equipo la lista con el tipo de personaje, asi si me lo decteta cuales son atributos y metodos.

lista_heroes.append(Personaje_1)
lista_heroes.append(personaje_2)
lista_heroes.append(personaje_3)
lista_heroes.append(personaje_4)

for heroe in lista_heroes:
    print(f"Lista de heroes : {heroe.describirse()}")

lista_heroes.pop(2)

for heroe in lista_heroes:
    print(f"Lista de heroes - 1 : {heroe.describirse()}")