import math

class Retangulo():
    def __init__(self, altura, largura):
        self._altura = altura
        self._largura = largura

    def calcArea(self):
        return self._altura * self._largura
    

class Quadrado(Retangulo):
    def __init__(self, lado):

        super().__init__(lado, lado)

retangulo1 = Retangulo(25, 40)
print(retangulo1.calcArea())

quadrado1 = Quadrado(25)
print(quadrado1.calcArea())

class Circle():
    def __init__(self, raio):
        self._raio = raio

    def calcArea(self):
        return math.pi * self._raio**2
    
    def calcCircunferencia(self):
        return 2*math.pi * self._raio
    
    def calcDiametro(self):
        return self._raio * 2
    

class Cilindro(Circle):
    def __init__(self, raio, altura):  
        super().__init__(raio)
        self._altura = altura

    def calcArea(self):
        return 2*math.pi * self._raio * self._altura

    def calcVolume(self):
        return math.pi * self._raio**2 * self._altura
    
    
circulo1 = Circle(5)

print(round(circulo1.calcArea(), 2))
print(round(circulo1.calcCircunferencia(), 2))
print(circulo1.calcDiametro())

cilindro1 = Cilindro(15, 7)
print(round(cilindro1.calcVolume(), 2))
print(round(cilindro1.calcArea(), 2))