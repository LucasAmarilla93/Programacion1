from Input import *

class Boligrafo:
    def __init__(self, grosor: str, color: str): #toda clase debe tener un constructor que deba tener inicializados los valores de la clase.
        self.capacidad_maxima = 100
        self.grosor = grosor
        self.color = color
        self.cantidad_tinta = 80

    def escribir(self) -> str: #me pasan un texto y tengo que ver si la tinta alcanza.
        #cantidad tinta = 80
        #trazo fino, gasta 1 por cada caracter.
        #trazo grueso, gasta 2 por cada caracter.
        texto = get_str("Ingrese su mensaje: ", "Reingrese un texto válido: ") #Este tiene que ser un get_str_
        tinta_a_gastar = 0
        match self.grosor:
            case "fino":
                tinta_a_gastar = len(texto)
            case "grueso":
                tinta_a_gastar = len(texto) * 2

        while self.cantidad_tinta < tinta_a_gastar:
            mensaje = "No alcanza la tinta"
            break
        
        self.cantidad_tinta = self.cantidad_tinta - tinta_a_gastar
        
        print(f"La cantidad de tinta restante es: {self.cantidad_tinta}")

        if self.cantidad_tinta > 0 :
            mensaje = f"Su mensaje es: {texto}"

        return mensaje
     
    
    def recargar(self) -> str:
        #tinta_parametro = 
        tinta_nueva = get_int("Ingrese la cantidad de tinta a recargar: ", "Ingrese una cantidad en digitos: ")
        mensaje = ""
        self.cantidad_tinta += tinta_nueva #Sumo la tinta pero si supera, no va.
        if self.cantidad_tinta > self.capacidad_maxima: #140 - 100
            mensaje = f"Se recargó la lapicera y sobró {self.cantidad_tinta - self.capacidad_maxima} de tinta"
            self.cantidad_tinta = self.capacidad_maxima #establezco la cantidad de tinta en 100 que es su capacidad maxima.
        else:
            mensaje = f"Lapicera recargada"
        
        return mensaje
