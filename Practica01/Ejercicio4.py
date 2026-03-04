#Estadistica
#jessica valkiria mayda apaza
#0.1 04/03/26
import math

class Estadistica:
    def __init__(self, datos):
        self.datos = datos

    def promedio(self):
        return sum(self.datos) / len(self.datos)

    def desviacion(self):
        prom = self.promedio()
        suma = 0
        for x in self.datos:
            suma += (x - prom) ** 2
        return math.sqrt(suma / (len(self.datos) - 1))

print("Ingrese 10 números separados por espacio:")
entrada = input()
numeros = entrada.split()
for i in range(len(numeros)):
    numeros[i] = float(numeros[i])

estadistica = Estadistica(numeros)

print("El promedio es", round(estadistica.promedio(), 2))
print("La desviación estandar es", round(estadistica.desviacion(), 5))
