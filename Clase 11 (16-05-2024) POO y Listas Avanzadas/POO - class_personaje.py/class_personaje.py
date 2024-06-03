#Definir como va a ser el objeto y las acciones del objeto.


#Ver video 9.30

#Dentro de los metodos de una clase, existe el constructor: que nos permite inicializar todos los atributos con un valor.

#Metodo constructor: es una funcion constructura. En Python se define como __init__(parametros) ->parametros que yo quiero inicializar y la palabra reservada self. Todos los metodos que defino empienzan con self.

class Personaje:
    #ATRIBUTOS
    #nombre -usa_nano - puede_volar - super_poder - poder_pelea

    #METODOS
    def __init__(self, nombre: str, nano: bool, vuela: bool, poder: str, pelea: int): #paso todos los parametros junto al self.
        #Atraves de ese self, voy a inicializar los valores.
        #El self es como agarrar una galletita en ese momento especificio y ponerlo dentro del cortante. 
        #Es para definir las instancias.
        self.nombre = nombre #El valor que venga al nombre, lo voy a guardar en el nombre. 
        self.usa_nanotecnologia = nano
        #self es la instnacia, usa_nanotecnologia es el atributo y el valor es nano
        self.puede_volar = vuela
        self.super_poder = poder
        self.poder_pelea = pelea
    #Ese seria el constructor definido.

    #Que el personaje se pueda describir.

    #def describirse(self): #El objeto conoce todo sus atributos, asi que solo recibo la instancia.
    #    print(f"{self.nombre} - {self.super_poder} - {self.poder_pelea}") #Me quedo con estos 3 porque los otros son booleanos.
        
    #Dentro del metodo puede haber logica.

    #Hacer a metodo describirse reutilizable.
    def describirse(self) -> str: #El objeto conoce todo sus atributos, asi que solo recibo la instancia.
        cadena = (f"{self.nombre} - {self.super_poder} - {self.poder_pelea}")
        if self.usa_nanotecnologia:
            cadena += " - Usa nanotecnologia"
        else:
            cadena += " - No usa nanotecnologia"
        
        return cadena

#Existen los metodos de clase que no necesitan la instancia.

    def volar(self, altura, velocidad):
        if self.puede_volar:
            print(f"Estoy volando a {altura} mts de altura, a una velocidad de {velocidad} Km/H")
        else:
            print(f"{self.nombre} usted no puede volar")


    def atacar(self, enemigo: 'Personaje'): #---> si quiero poner una clase cuando estoy dentro de otra clase, lo pongo entre comillas. --> lo hago con las comillas al lado del 0.
        if self.poder_pelea > enemigo.poder_pelea:
            print(f"GANO {self.nombre}")
            self.poder_pelea -= enemigo.poder_pelea #Digo que le resto el poder de pelea del que ataco y gano.
            enemigo.poder_pelea = 0 #poder de pelea del que perdio y quedo en 0        elif self.poder_pelea > enemigo.poder_pelea:
        elif self.poder_pelea < enemigo.poder_pelea:    
            print(f"GANO {enemigo.nombre}")
            enemigo.poder_pelea -= self.poder_pelea
            self.poder_pelea = 0
        else :
            print("EMPATARON") #Como empataron me quedo con el 90 porciento de pelea de cada uno.
            enemigo.poder_pelea *= 0.9
            self.poder_pelea *= 0.9


    #los atributos de una clase tienen que ser privados, yo afuera de una clase no puedo acceder a un atributo para mantener el encapsulamiento.

    #las propiedades: puede modificar atributos, es una forma de acceder a los atributos para leerlos o escribirlos. 