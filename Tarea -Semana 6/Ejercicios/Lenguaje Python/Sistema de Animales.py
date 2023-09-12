'''
Sistema de Animales
Crear una clase base Animal con atributos como nombre y edad, y un método sonido que deberá ser implementado por las clases derivadas.
Crear clases derivadas para diferentes tipos de animales, como Perro, Gato y Pájaro, cada una con una implementación única del método sonido.
'''
class Animales:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad 
    def sonido(self): 
        print('Sonido')   # arreglar revidar
class Perro(Animales):
    def sonido(self):
        print('Ladrar: wool wool')
class Gato(Animales):
    def sonido(self):
        print('Ronronear: rrr rrr rrr rrr')
class Pajaro(Animales):
    def sonido(self):
        print('Cantar: la la la la')

Perro_1 = Perro('Pedrito',4)
Gato_1 = Gato('Mermelada',3)
Pajaro_1 = Pajaro('Timoteo',2)
for x in (Perro_1,Gato_1,Pajaro_1):
    x.sonido()

