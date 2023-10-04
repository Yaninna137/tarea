#3.Desarrolle en alg´un lenguaje de programaci´on un sistema de gesti´on universitaria. (6)
# • Las clases que debe tener el sistema de gesti´on universitaria son: Persona, Estudiante,
# Profesor, Asignatura, Grupo y ProgramaAcademico,
# • Recuerde hacer uso de atributos y m´etodos.
# • Recuerde hacer uso de herencia.

#               Sistema_GestionU 

class Personas:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def presentacion(self,tipo = 'Persona'):
        return 'Mi nombre es {} {} y tengo {} años y soy {}'.format(self.nombre,self.apellido,self.edad,tipo)
class Profesor(Personas):
    def presentacion(self):
        return super().presentacion('Profesor') 
class Estudiante(Personas):
    def presentacion(self):
        return super().presentacion('Estudiante') 


# Codigo de prueba de estas clases , verificación de herencia
P = Profesor('Max','CANT',24)
e = Estudiante('Alex','Sent',12)
print(e.presentacion())
print(P.presentacion())
