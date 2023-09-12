'''
Sistema de Reservas de Vuelos
Crear una clase base Reserva que contenga atributos como nombre_del_pasajero, número_de_vuelo y fecha.
Crear clases derivadas como ReservaEconómica, ReservaBusiness y ReservaPrimeraClase que hereden de Reserva y que contengan atributos y métodos únicos para cada tipo de reserva.
Implementar un método mostrar_detalle en cada clase para mostrar los detalles de la reserva de una forma única dependiendo del tipo de clase de reserva.
'''
class Reserva:
    def __init__(self,nombre_del_pasajero,numero_de_vuelo,fecha):
        self.nombre_p = nombre_del_pasajero
        self.num_vuelo = numero_de_vuelo
        self.fecha = fecha
    def mostrar_detalle(self):
        print('Reserva')
class ReservaEconomica(Reserva):
    pass
class ReservaBusiness(Reserva):
    pass
    #Reservas para larga distancia
class ReservaPrimeraClase(Reserva):
    pass
    #Reservas mas caras