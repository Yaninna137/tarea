'''
Sistema de Empleados de una Empresa
Crear una clase base Empleado que contenga atributos como nombre, edad y salario.
Crear clases derivadas como Gerente, Ingeniero y Asistente con atributos y métodos únicos para cada rol.
Implementar un método describir_rol en cada clase para describir el rol de un empleado de una manera que sea específica para su posición.
'''
class Empleados:
    def __init__(self,nombre,edad,salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def describir_rol(self):
        print('El rol es...')
class Gerente(Empleados):
    def __init__(self,nombre,edad,salario,nivel_desempeño):
        super().__init__(nombre,edad,salario)
        self.nivel = nivel_desempeño
    def describir_rol(self):
        rol = ''' El Gerenste {} tiene el rol de Organizar los recursos de la entidad. 
        Definir a donde se va a dirigir la empresa en un corto, medio y largo plazo, entre otras muchas tareas.
        Fijación de una serie de objetivos que marcan el rumbo y el trabajo de la organización. Y el despeña un nivel de {}'''.format(self.nombre,self.nivel)
        print(rol)

class Ingeniero(Empleados):
    def __init__(self,nombre,edad,salario):
        super().__init__(nombre,edad,salario)
    def describir_rol(self):
        rol = ''' El Gerenste {} tiene el rol de Un ingeniero tiene la mirada y formación integradora para conseguir
          objetivos de desarrollo sostenible en la planificación, diseño, fabricación, gestión, administración y 
          control de calidad de un producto o sistema'''.format(self.nombre)
        print(rol)

class Asistente(Empleados):
    def __init__(self,nombre,edad,salario):
        super().__init__(nombre,edad,salario)
    def describir_rol(self):
        rol = ''' El Gerenste {} tiene el rol de ayudar a los directivos hacer un mejor uso de su tiempo, por ejemplo, 
        atendiendo a sus llamadas telefónicas y correo electrónico, gestionando su agenda, programando citas, e 
        investigando y resumiendo la información pertinente para la preparación de reuniones.'''.format(self.nombre)
        print(rol)
    
gerente_1 = Gerente('Angel', 30, 900000,'Alto')
inginiero_1 = Ingeniero('Carlos',40,800000)
asistente_1 = Asistente('Fiona',28,850000)

for x in (gerente_1,inginiero_1,asistente_1):
    x.describir_rol()
    print('\n')