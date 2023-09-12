'''
Sistema de Gestión de Productos
Crear una clase base Producto que contenga atributos como nombre, precio y categoría.
Crear clases derivadas para diferentes tipos de productos como Electrónico, Alimenticio y Vestimenta. Añadir atributos únicos para cada clase derivada.
Implementar un método llamado mostrar_detalle en cada clase para mostrar los detalles del producto de una manera única para cada tipo de producto.
'''
class Productos:
    def __init__(self,nombre,precio,categoria):
        self.nombre = nombre 
        self.precio = precio 
        self.categoria = categoria
    def mostrar_detalle(self):
        print('Mostrar los detalles')
class Electrónicos(Productos):
    def __init__(self,nombre,precio,categoria,consumo_de_wat):
        super().__init__(nombre,precio,categoria)
        self.consumo_WATT = consumo_de_wat
    def mostrar_detalle(self):
        print('{}/ {}  |$ {} |\nConsume un {} de watt por hrs.'.format(self.nombre,self.categoria,self.precio,self.consumo_WATT))
class Alimenticio(Productos):
    def __init__(self, nombre, precio, categoria,fecha_elevoracion,fecha_vencimiento):
        super().__init__(nombre, precio, categoria)
        self.felav = fecha_elevoracion
        self.fven = fecha_vencimiento
    def mostrar_detalle(self):
        print('---Categoria "{}"--\nProducto: {}\n\t|$ {} |\nFecha elevoracion {}\nFeha vencimiento {}'.format(self.categoria,self.nombre,self.precio,self.felav,self.fven))

class Vestimenta(Productos):
    def __init__(self, nombre, precio, categoria,codigo_de_barra,talla):
        super().__init__(nombre, precio, categoria)
        self.cod_b = codigo_de_barra
        self.talla = talla
    def mostrar_detalle(self):
        print('El {} de talla {} cuesta $ {} {} \n {}/{}/Vestidos/{}'.format(self.nombre,self.talla,self.precio,('Es algo caro,hay algunos con menor precio D:'if self.precio > 30000 else 'Un producto muy conveniente para tus ahorros :D'),self.nombre,self.categoria,self.cod_b))

electrónicos_1 = Electrónicos('Tostadora',60000,'electrico',300)
alimenticio_1 = Alimenticio('Arroz 1kl',1500,'Alimenticio','9 de agosto 2008','13 de octubre 2023')
vestimenta_1 = Vestimenta('Vestido',20000,'Vestimenta',1001010111010101,'XS')

for x in (electrónicos_1,alimenticio_1,vestimenta_1):
    x.mostrar_detalle()
    print('\n')
    