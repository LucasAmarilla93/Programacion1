
################################ Medir tiempo de algoritmo ######################################################

import time

array = [1,4,3,5,2]
#Antes de arrancar el algoritmo
start = time.time() # Me devuelve un valor numerico, un instante en el tiempo. (expresado en milisegundos)


for i in range(0, len(array) - 1):
    for j in range (i + 1, len(array)):
        if array[i] < array [j] :
            auxiliar = array[i]
            array[i] = array [j]
            array[j] = auxiliar

end = time.time() #Tiempo en el que finaliza. 

print(start)
print(end) #La lista es pequeña y no tardo nada en ordenarlo. 
print(array)

print(end - start) #Me devuelve 0 pero no es la realidad ya que algo de tiempo demoro, pero esta forma de hacerlo no me deja verlo.
#Le paso una lista mas grande. 

# 1 ms -- 0.001s
# al resultado lo * 1000