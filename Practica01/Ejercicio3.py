#Algebra ecuaciones
#jessica valkiria mayda apaza
#0.1 04/03/26
import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getDiscriminante(self):
        return self.b**2 - 4*self.a*self.c

    def getRaiz1(self):
        if self.getDiscriminante() >= 0:
            return (-self.b + math.sqrt(self.getDiscriminante())) / (2*self.a)
        else:
            return 0

    def getRaiz2(self):
        if self.getDiscriminante() >= 0:
            return (-self.b - math.sqrt(self.getDiscriminante())) / (2*self.a)
        else:
            return 0



a,b,c,= map(float,input("Ingrese a,b,c: ").split())

ecuacion = EcuacionCuadratica(a, b, c)
d = ecuacion.getDiscriminante()

if d > 0:
    print("La ecuación tiene dos raíces", ecuacion.getRaiz1(), "y", ecuacion.getRaiz2())
elif d == 0:
    print("La ecuación tiene una raíz", ecuacion.getRaiz1())
else:
    print("La ecuación no tiene raíces reales")
