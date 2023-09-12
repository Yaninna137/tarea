'''
Desafío
Sistema de Gestión Universitaria
Desarrolle un sistema para gestionar una universidad que tenga las siguientes características:

Clase Persona:
Atributos: nombre, apellido, fecha_de_nacimiento.
Métodos: presentarse, que deberá imprimir una presentación genérica de una persona.
'''
class Personas:
    def __init__(self,nombre,apellido,fecha_de_nacimiento): 
        self.nombre = nombre
        self.apellido = apellido
        self.f_n = fecha_de_nacimiento
    def presentarse(self):
        print(f'Hola soy un humano que se llama {self.nombre} {self.apellido}.y que nacio el {self.f_n}')
'''
Clase Estudiante (hereda de Persona):
Atributos: matrícula, carrera, semestre.
Métodos:
estudiar: recibirá una materia y horas de estudio y imprimirá un mensaje indicando que el estudiante ha estudiado dicha materia durante X horas.
presentarse: deberá sobrescribir el método de la clase Persona para incluir información del estudiante.
''' 
class Estudiante(Personas):
    def __init__(self, nombre, apellido, fecha_de_nacimiento,matricula,carrera,semestre):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self.matricula = matricula
        self.carrera = carrera
        self.semetre = semestre 
    def Estudiar(self,materia,hrs_estudio):
        print('El estudiante "{} {}" ah estudiado {} por {} hrs{}'.format(self.nombre,self.apellido,materia,hrs_estudio,('Lo cual es grandiaso , pero a la proxima procure tomar descansos entre medio :)'if hrs_estudio >=7 else 'Un gran Logro')))
    def presentarse(self):
        print(f''''
              Hola! Me presento :D
              Mi nombre es {self.nombre} {self.apellido}.Y soy un estudiante.
              Estoy en la carrera {self.carrera} y voy en el semestre {self.semetre} de mi carrerra
              .Un dato extra es que naci el {self.f_n} y tengo la matricula {self.matricula}.
              ''')
'''
Clase Profesor (hereda de Persona):
Atributos: número_empleado, departamento.
Métodos:
enseñar: recibirá una materia y imprimirá un mensaje indicando que el profesor está enseñando dicha materia.
presentarse: deberá sobrescribir el método de la clase Persona para incluir información del profesor.
'''
class Profesor(Personas):
    def __init__(self, nombre, apellido, fecha_de_nacimiento,numero_empleado,departamento):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self.num_empl = numero_empleado
        self.departamento = departamento
    def Enseñar(self,materia):
        print('El profesor {} ésta enseñando la materia {}'.format(self.nombre,materia))
    def presentarse(self):
        print(f''''
              Hola.Soy el docente {self.nombre} {self.apellido}.Naci el {self.f_n} y soy Profesor
              del departamento {self.departamento}.En lo largo de mi vida eh contado con
              {self.num_empl} empleos.
              ''')  
'''
Clase Asignatura:
Atributos: nombre, código, créditos.
Métodos: mostrar_información: imprimirá la información de la asignatura.
'''
class Asignatura(Personas):
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.credito = creditos
    def mostrar_información(self):
        print(f"La asiganatura '{self.nombre}' consta con {self.credito} creditos.|CÓDIGO: {self.codigo}|")
'''
Clase Grupo:
Atributos: número_grupo, asignatura (un objeto de tipo Asignatura), profesor (un objeto de tipo Profesor), estudiantes (una lista de objetos de tipo Estudiante).
Métodos:
agregar_estudiante: permitirá agregar un estudiante al grupo.
eliminar_estudiante: permitirá eliminar un estudiante del grupo.
mostrar_grupo: mostrará la información del grupo incluyendo el profesor asignado y la lista de estudiantes.
'''
class Grupo:
    def __init__(self,número_grupo, Asignatura, Profesor , Estudiantes ):
        self.num_grupo = número_grupo           # numero 
        self.asignatura = Asignatura            # 1 objeto
        self.profesor = Profesor                # 1 objeto
        self.estudiante = Estudiantes   #Listas de objetos de Estudiantes
    def Agregar_estudiante(self,Estudiante):
        self.estudiante.append(Estudiante)
        print('Estudiante nuevo agregado')   #####################################
    def Eliminar_estudiante(self,Estudiante):
        for Estudiante_En_Grup in self.estudiante:
            if Estudiante_En_Grup.nombre == Estudiante.nombre and Estudiante_En_Grup.apellido == Estudiante.apellido and Estudiante_En_Grup.carrera == Estudiante.carrera:
                print('Estudiate {} ha sido eliminado del grupo'.format(Estudiante_En_Grup.nombre))
                self.estudiante.remove(Estudiante_En_Grup)
                #Estudiante eliminado
    def mostrar_grupo(self):
        print('---------------GROUP : {}N°----------------'.format(self.num_grupo))
        print('Profesor {} {} | Conformado: {} Estudiantes '.format(self.profesor.nombre,self.profesor.apellido,len(self.estudiante)))
        for i in range(len(self.estudiante)):
            print(i +1,f'¬ {self.estudiante[i].nombre} {self.estudiante[i].apellido} |CARRERA: {self.estudiante[i].carrera}')
'''
Clase ProgramaAcademico:
Atributos: nombre, codigo, grupos (una lista de objetos de tipo Grupo).
Métodos:
agregar_grupo: permitirá agregar un grupo al programa académico.
eliminar_grupo: permitirá eliminar un grupo del programa académico.
mostrar_programa: mostrará la información del programa académico incluyendo todos los grupos con su respectiva información.
'''
class ProgramaAcademico:
    def __init__(self,nombre,codigos,Grupos):
        self.nombre = nombre 
        self.codigos = codigos 
        self.Grupos = Grupos     # Lista de objetos grupos 
    def Agregar_grup(self,Grupo):
        self.Grupos.append(Grupo)
        print('Grupo nuevo agregado')   #####################################
    def Eliminar_grupo(self,Grupo):
        for Grupo_indv in self.Grupos:
            if Grupo_indv.num_grupo == Grupo.num_grupo and  Grupo_indv.asignatura == Grupo.asignatura:
                print('Grupo {} ha sido eliminado del grupo'.format(Grupo_indv.num_grupo))
                self.Grupos.remove(Grupo_indv)
    def mostrar_programa(self):
        print('---------------|PROGRAMA ACADEMICO : {}N°|CODE: {} |----------------'.format(self.nombre,self.codigos))
        print('Codigo {}  | Conformado: {} N° '.format(self.codigos,len(self.Grupos)))
        for i in range(len(self.Grupos)):
            print(f'./{self.Grupos[i].num_grupo}/Asignatura:{self.Grupos[i].asignatura.nombre}/Profesor: {self.Grupos[i].profesor.nombre} {self.Grupos[i].profesor.apellido} /Total de Estudiantes: {len(self.Grupos[i].estudiante)}')
''' 
Desarrolle un script que cree varias instancias de estas clases y demuestre la interacción entre ellas a través de los diferentes métodos implementados.
'''
# persona = Personas('Nombre','Apellido','11 de septiembre del 2023')

# estudiante_1 = Estudiante('Angel','Cruz','9 de agosto 2004','Matricula 01','Informatica',4)
# estudiante_2= Estudiante('Antonio','Camino','12 de julio 2002','Matricula 01','Informatica',2)
# estudiante_3 = Estudiante('Alexis','Canella','20 de febrero 2003','Matricula 01','Informatica',2)
# estudiante_4 = Estudiante('Aron','Callampa','1 de septiembre 2003','Matricula 01','Informatica',4)
# estudiante_5 = Estudiante('Abel','Contreras','18 de diciembre 2004','Matricula 01','Informatica',4)

# p_rofesor = Profesor('Pablo','Hernandez','8 de julio 1990',20,'Matematicas')
# p_rofesor_1 = Profesor('Xiomara','Lirus','1 de febrero 1980',12,'literatura')
# p_rofesor_2 = Profesor('Esteban','Zapata','18 de agosto 1987',24,'Complejidad Alg.')

# a_signatura = Asignatura('Algebra',23452,7)
# a_signatura_2 = Asignatura('Literatura',23452,7)

# g_rupo = Grupo(1,a_signatura,p_rofesor,[estudiante_1,estudiante_2,estudiante_3,estudiante_4,estudiante_5])
# g_rupo_1 = Grupo(2,a_signatura,p_rofesor_2,[estudiante_2,estudiante_1,estudiante_3,estudiante_4,estudiante_5])
# g_rupo_2 = Grupo(3,a_signatura_2,p_rofesor_1,[estudiante_5,estudiante_4,estudiante_3,estudiante_2,estudiante_1])
# g_rupo_3 = Grupo(4,a_signatura_2,p_rofesor_2,[estudiante_2,estudiante_1,estudiante_3,estudiante_5,estudiante_4])
# persona.presentarse()          # Verificar la creacion de la clase persona llama ndo su funcion
# estudiante_1.Estudiar('Matematicas',8)   # Verificar el metodo si funciona  estudiante_1.Estudiar('Matematicas',6) , dependiendo del numero de hrs que se ingrrese te saldra un mensaje.
# estudiante_1.presentarse()               # Verificando si imprimi en pantalla con los datos coorectos
# p_rofesor.Enseñar('Mates')          # accion de enseñar para profesor 
# p_rofesor.presentarse()             # mostrar presentacion del profesor 
# a_signatura.mostrar_información()           # mostar imformacion por consola
# g_rupo.mostrar_grupo()                      # mostar una lista de los grupos que hay
# g_rupo.Agregar_estudiante(estudiante_4)      # agreagr estudiante al grupo
# g_rupo.mostrar_grupo()                       # mostar grupo para verficar
# g_rupo.Eliminar_estudiante(estudiante_4)     # eliminar estudiante del grupo 
# g_rupo.mostrar_grupo()                       # 

# p_acad = ProgramaAcademico('Prog.Academica','#101210',[g_rupo,g_rupo_1,g_rupo_2,g_rupo_3])
# p_acad.Agregar_grup(g_rupo)
# p_acad.Eliminar_grupo(g_rupo)
# p_acad.mostrar_programa()
'''
Consideraciones adicionales:

Implemente validaciones necesarias para evitar inconsistencias (como eliminar un estudiante que no existe en un grupo).
Implemente una interfaz textual que permita a un usuario interactuar con el sistema (crear objetos, asignar estudiantes a grupos, etc.).
Incluya comentarios y docstrings que expliquen su código adecuadamente.
'''
class Almamiento:
    def __init__(self):
        self.Personas = 0           # Contar cuantas personas hay
        self.A_Est = []             # Lista de alamacenamineto de Estudiantes
        self.A_Prof = []            # Lista de alamacenamineto de Profesores
        self.A_Asig= []             # Lista de alamacenamineto de Asiganturas
        self.A_Grupos = []          # Lista de alamacenamineto de Grupos
        self.A_ProgA = []           # Lista de alamacenamineto de ProgramaAcademico:
    def buscar_estudiante_GRUP(self,Grupo,Estudiante):
        for estud in Grupo.estudiante:
            if estud.nombre == Estudiante.nombre and estud.apellido == Estudiante.apellido and estud.f_n == Estudiante.f_n : # Verificar cada estudiante del grupo con el estudiante que se esta buscando.
                return True # En caso de cumplir retorna True
        return False # En caso de no encontrar dicho estudiante retorna falso
    
    def verificar_limites_de_agregar_una_GRUP(self,Grupo_que_se_quiere_agregar):
        for grup_indv in self.A_Grupos:
            if grup_indv.num_grupo == Grupo_que_se_quiere_agregar.num_grupo:
                return False # retornara falso , porque el numero que se ingreso en el nuevo grupo ya existe, dentro de los grupos agregados.
        return True # El numero no existe.Por ende es valido.

        # para poder buscar al grupo se podria crear una condicional de limites de cuantos grupos se agregaran , como los numeros disponibles 

    
# Funciones para porder implementar el "interfaz textual que permita a un usuario interactuar con el sistema" llamando funciones.
def Sistema_Estudiantes():
    pass
def Sistema_Profesor():
    pass
def Sistema_Asigantura():
    pass
def Sistema_Grupo():
    pass
def Sistema_ProgramaAcademico():
    pass
