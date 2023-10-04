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
        return('Detalles de Reseva')
class ReservaEconomica(Reserva):
    def __init__(self,nombre_p, num_vuelo, fecha,Programa_de_Millas):
        super.__init__(nombre_p,num_vuelo,fecha)
        self.millas = Programa_de_Millas
    def mostrar_detalle(self):
        return '''
        -----------------------------------------------------------------------
            Ticket: Reserva Economica {}
            Nombre Pasajero:{}
            Vuelo: {} N-°
            Fecha de reserva: {}
            Cuenta con millas : {}
        ----------------------------------------------------------------------
            '''.format(self.nombre_p,self.num_vuelo,self.fecha,('Si' if self.millas == True else 'No'))
class ReservaBusiness(Reserva):
    def __init__(self,nombre_p, num_vuelo, fecha,Comida_en_especifico):
        super.__init__(nombre_p,num_vuelo,fecha)
        self.Comida_especifico = Comida_en_especifico
    def mostrar_detalle(self):
        return '''
        ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡
            Ticket: Reserva Busines {}
            Nombre Pasajero: {}
            Vuelo: {} N-°
            Fecha de reserva: {}
            Tipo de comida solicitada para el vuuelo: {}
        ¡ ¡ ¡ ¡  ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡ ¡
            '''.format(self.nombre_p,self.num_vuelo,self.fecha,self.Comida_especifico)
        
class ReservaPrimeraClase(Reserva):
    def __init__(self,nombre_p, num_vuelo,fecha,servicio_personal = False):
        super.__init__(nombre_p,num_vuelo,fecha)
        self.servicio_per= servicio_personal
        if self.servicio_per == True:
            self.Tipo_de_servicio = 'Su reserva cuenta con servicio personal,1 asistente personal y atencion: media(Personalizar(Servicio_personal))'
        else:
            self.Tipo_de_servicio = 'Su reserva no cuenta con servicio personal'
    def mostrar_detalle(self):
        return '''
        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
            Ticket: Reserva Primera Clase {}
            Nombre Pasajero:{}
            Vuelo: {} N-°
            Fecha de reserva: {}
            {}
        + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
            '''.format(self.nombre_p,self.num_vuelo,self.fecha,self.Tipo_de_servicio)
    def Servicio_Personal(self):
        if self.servicio_per == True:
            a = input('Que nivel de atención(alta,media,baja): ')
            b = input('Asintente personal(1 o más): ')
            self.Tipo_de_servicio = 'Su reserva cuenta con servicio Personal \n Incluye {} de asistentes personal\n Con un nivel {} de atención'.format(a,b)
        else:
            a = bool(int(input('Activar servicio personal(0)no (1)si: ')))
            if a == True:
                if True != self.Servicio_Personal:
                    a = input('Que nivel de atención(alta,media,baja): ')
                    b = input('Asintente personal(1 o más): ')
                    self.Tipo_de_servicio = 'Su reserva cuenta con servicio Personal \n Incluye {} de asistentes personal\n Con un nivel {} de atención'.format(a,b)
                    return 'Servicio personal activado'
                else:
                    return 'Ya esta con el servcio personal' 
            else:
                return 'Sin cambios'
    
Reserva_1 = ReservaEconomica('Juanito Mellado',3,'16 de octubre 2024',True)
Reserva_2 = ReservaBusiness('Pedrito Colon',4,'3 de diciembre 2023','Mariscos')
Reserva_3 = ReservaPrimeraClase('Guillerno Contreras',1,'4 nombiembre 2023',True)
for reservas in (Reserva_1,Reserva_2,Reserva_3):
    print(reservas.mostrar_detalle())