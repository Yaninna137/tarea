import time
import random as rd
class Playlist:
    def __init__(self,nombre,arreglo):
        self.nombre = nombre                                 # Debe poseer un atributo "nombre". Este será la referencia al nombre de la lista de reproducción
        self.listas_contenedor_de_song = arreglo              # Un atributo que contendrá las canciones; se espera que sea un arreglo de strings
        self.Estado = ['Reproduciendo','Pausa','Detenido']   # Un atributo que representará el estado. Los estados pueden ser: reproduciendo, pausa y detenido
        self.indice_cancion = None

    def Añadir_cancion(self,cancion):                       # Un método que permitirá añadir una canción.
        self.listas_contenedor_de_song.append(cancion)      ## usando una funcion append se agregaran las nuevas caniones.

    def Eliminar_cancion(self,cancion):                     #Un método que permitirá eliminar una canción.
        self.listas_contenedor_de_song.remove(cancion)       #eliminar una la cancion ,atraves de la funcion remove

    def Mostrar_Todas_las_canciones(self):                 # Un método que permitirá mostrar todas las canciones.
        for x in range(len(self.listas_contenedor_de_song)):
            print(x,'¬. ',self.listas_contenedor_de_song[x])

    def Comienza_a_reproducir_cancion(self,arreglo):
        for x in range(len(arreglo)):                       # reproducira la cancion
            time.sleep(10)
    def Selccionar_una_cancion_a_reproducir(self,indice):
        return self.listas_contenedor_de_song[indice]             # con el indice selecciona la posiscio ah reproducir

    def Pausar_cancion(self,indice):
        return 
    def Detener_la_reproduccion():
        pass
    def Pasar_sig_cancion():
        pass
    def Retroceder_cancion_anterior(self,cancion):
        index = self.listas_contenedor_de_song.index(cancion)
        return index - 1                                          # retornar el indice de la anterior cancion
    def Reproducir_una_cancion_aleatoria(self):
        # ''' (si ya está reproduciendo una canción, 
        #     al seleccionar una canción aleatoria no puede 
        #     reproducir la que ya se estaba reproduciendo).'''
        len_lista = len(self.listas_contenedor_de_song)
        indice_de_reproducion = [i for i in range(len_lista)]
        # desordenar lista  // arrglar con un algoritmo , eficas 
        lista = []
        i = 0
        while i <= len(lista):
            numero_aleatorio = rd.randrange(len_lista)
            if numero_aleatorio not in lista:
                lista.append(numero_aleatorio)
                i += 1
        return lista                    # retornar una lista con los indices de cada cancion pero desordenada
    
    def Ver_estado_Playlist(self,num_estado_pregunta):
        if num_estado_pregunta == 0:
            return 'Esta playlist esta en {}'.format(self.Estado[0])
        if num_estado_pregunta == 1:
            return 'Esta playlist esta en {}'.format(self.Estado[1])
        if num_estado_pregunta == 2:
            return 'Esta playlist esta en {}'.format(self.Estado[2])      
          
    def Ver_cancion_reproduciendo(self,indice_reproducion):
        return f'La cancion que se esta REPRODUCIENDO es: {self.listas_contenedor_de_song[indice_reproducion]}'

canciones = ['musica pop','musica clasica','musica rok','musica electrica','musica jazz']
My_musica = Playlist('XXLL',canciones)
My_musica.Comienza_a_reproducir_cancion()

def comando_de_playlist(objeto):
    input('REproducir(0) , Pausar una cancion(1), Detener(2), Sig.Cancion(3), Retroceder(4)','R.ALEATORIA' )


# start = False
# while not start:
#     print(f'Bienvenido a tu {My_musica.nombre}')
#     input('')
