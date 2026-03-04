#Cronometro
#jessica valkiria mayda apaza
#0.1 04/03/26i
import time
import random

class Cronometro:
    def __init__(self):
        self.inicia = time.time()
        self.finaliza = 0   

    def getInicia(self):
        return self.inicia

    def getFinaliza(self):
        return self.finaliza

    def iniciaCrono(self):
        self.inicia = time.time()

    def detener(self):
        self.finaliza = time.time()

    def lapsoDeTiempo(self):
        if self.finaliza != 0:   
            return (self.finaliza - self.inicia) * 1000000
        else:
            return 0
def ordenacion_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_indice = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_indice]:
                min_indice = j

        aux = lista[i]
        lista[i] = lista[min_indice]
        lista[min_indice] = aux


numeros = [random.randint(1, 1000000) for _ in range(10000)]

crono = Cronometro()
crono.iniciaCrono()
ordenacion_seleccion(numeros)
crono.detener()

print("Tiempo en milisegundos:", crono.lapsoDeTiempo())
