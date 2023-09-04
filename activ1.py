import math
class Circulo:

    def __init__(self,radio):
        self.radio = radio

    def calcularArea(self):
        return round(math.pi * (self.radio**2),3)    # numero pi * r^2
    def calcularPerimetro(self):            # 2 * numero pi
        return round((2 * math.pi * self.radio),3)
   
    def camabiarRadio(self,new_radio):  
        self.radio = new_radio

circulo = Circulo(10)
# print(circulo.calcularArea())
# print(circulo.calcularPerimetro())  
print(circulo.radio)




class Rectangulo:
    def __init__(self,longitud,ancho):
        self.longitud = longitud
        self.ancho = ancho
    def calcularArea(self):
        return self.longitud * self.ancho
    def calcularPerimetro(self):            # 2 * numero pi
        return (2 * self.longitud) + (2 * self.ancho)
    def camabiarLongitud(self,Longitud):  
        self.longitud = Longitud
    def camabiarAncho(self,ancho):  
        self.ancho = ancho
rectangulo = Rectangulo(4,6)
# print(rectangulo.calcularArea())
# print(rectangulo.calcularPerimetro())