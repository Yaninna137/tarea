# 2.Desarrolle en algún lenguaje de programación un sistema para una librería. La librería debe
#   agregar y buscar libros basados en su título. Para hacer la búsqueda más eficiente, haga uso del
#   código del ejercicio 1.
class Libreria:
    def __init__(self,nombre_de_libreria):                                                
        self.nombre_L = nombre_de_libreria                                              #Atributo1: str: Contiene el nombre de la libreria
        self.tit_libros = ['juan','pedro','maria','ponce','mercado','manuel','edgar']   #Atributo2: Lista paralela1: Contiene los titulos
        self.id_libros = [1,2,4,7,9,10,11]                                              #Atributo3: Lista paralela2: Contiene los id de cad.libro

    def buscar_libros(self,x):   #Metodo1 : Algoritmo :Busqueda_binaria: Busca en la lista paralela2'id_libros' , cuando se tiene el id buscado entrega(retornara)
                                 #                           el titulo , lista_de_titulos[id_encontrado]
                                 # En caso de no encontrar el id , retorna un mensaje
        low = 0         
        high = len(self.id_libros)-1
        mid = 0

        while low <= high:
            mid = (high + low) //2
            if self.id_libros[mid] < x:
                low = mid + 1
            elif self.id_libros[mid] > x:
                high = mid - 1
            else:
                return self.tit_libros[mid]
        return f'No se encuentra ningún libro en el ide entregado'

lib = Libreria('Libreria-9029')
print(lib.buscar_libros(3))