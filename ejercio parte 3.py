import time
import keyboard
import random as rd
class Playlist:
    def __init__(self,nombre,arreglo):
        self.nombre = nombre                                 # Debe poseer un atributo "nombre". Este será la referencia al nombre de la lista de reproducción
        self.listas_contenedor_de_song = arreglo              # Un atributo que contendrá las canciones; se espera que sea un arreglo de strings
        self.Estado = 'Detenido'   # Un atributo que representará el estado. Los estados pueden ser: reproduciendo, pausa y detenido
        self.indice_cancion = 0           # se inicializa en 0 por defaout , ya que al iniciar este tendra 0 , para iniciar la play list                           # Un atributo que indica el índice de la canción que se está reproduciendo


    def Añadir_cancion(self,cancion):                       # Un método que permitirá añadir una canción.
        self.listas_contenedor_de_song.append(cancion)      ## usando una funcion append se agregaran las nuevas caniones.

    def Eliminar_cancion(self,cancion):                     #Un método que permitirá eliminar una canción.
        self.listas_contenedor_de_song.remove(cancion)       #eliminar una la cancion ,atraves de la funcion remove

    def Mostrar_Todas_las_canciones(self):                 # Un método que permitirá mostrar todas las canciones.
        for x in range(len(self.listas_contenedor_de_song)):
            print(x,'¬. ',self.listas_contenedor_de_song[x])

    def Comienza_Reproducir_cancion(self):                          # comienza a reproducir una canción
        self.Estado = 'Reproduciendo'
        return self.listas_contenedor_de_song[self.indice_cancion]
    
    def Selccionar_una_cancion_a_reproducir(self,indice):
        self.indice_cancion = indice                           # Cambiar el valor de la actual reproducion y colocar ah reproducir el nuevo

    def Pausar_cancion(self):
        self.Estado = 'Pausado'
        print('La cancion se encuentra pausada')
        m = input('Enter para dejar la pausa')
        self.Estado = 'Reproduccion'
    def Detener_la_reproduccion(self):
        self.Estado = 'Detenido'

    def Pasar_sig_cancion(self):
        self.indice_cancion += 1
        print('Siguiente...')
    def Retroceder_cancion_anterior(self):
        self.indice_cancion -= 1                                # retornar el indice de la anterior cancion
        print('Retrocediendo...')
    def Reproducir_una_cancion_aleatoria(self):
        lista = self.listas_contenedor_de_song
        len_lista = len(self.listas_contenedor_de_song)
        i = 0
        while len(lista) > i:
            numero_aleatorio = rd.randrange(len_lista)
            aux = lista[i]
            lista[i] = lista[numero_aleatorio]
            lista[numero_aleatorio] = aux
            i += 1          
    def Ver_estado_Playlist(self):
        return 'Esta playlist esta en {}'.format(self.Estado)      
    def Ver_cancion_reproduciendo(self,indice_reproducion):
        return f'La cancion que se esta REPRODUCIENDO es: {self.listas_contenedor_de_song[self.indice_cancion]}'
    #METODO PARA ELIMINAR OBJETO
    def __del__(self):
        print('objeto destruido')

# canciones = ['musica pop','musica clasica','musica rok','musica electrica','musica jazz']
# My_musica = Playlist('XXLL',canciones)
canciones = ['musica pop','musica clasica','musica jazz']
My_musica = Playlist('XXLL',canciones)
def menu():
    print('Bienvenido. Para manejar tu Playlist tienes los suiguintes opciones')
    print('A.Mostrar todas las canciones.')
    print('B.Eliminar una canción.')
    print('C.Añadir una canción')

    print('1.Reproducir una canción(0)')
    print('2.Reproducir una canción aleatoria ')
    print('3.Seleccionar una canción a reproducion(1)')
    print('4.Pausar una canción')
    print('5.Detener la reproducción')
    print('6.Siguiente canción')
    print('7retroceder a la canción anterior')
    print('8.estado de la playlist')
    print('9.Ver la canción que se está reproduciendo')
def menum():
    print("Bienvenido <(II)>")
    print("1.reproducir")
    print(" 'p' para pausar play list")
def comando_r(objeto):
    objeto.Estado = 'Reproduccion'
    tiempo_total_c = len(canciones) * 10
    i = j = 0
    TiempoC = 10
    while i < TiempoC and j <tiempo_total_c:

        if keyboard.is_pressed('p'):                         # Al precionar la tecla p se pausara la playlist
            objeto.Pausar_cancion()
        if objeto.Estado == 'Reproduccion':
            objeto.listas_contenedor_de_song[objeto.indice_cancion]
            time.sleep(1)
            print(i)
            i += 1
            j += 1
        if keyboard.is_pressed('p'):
            objeto.Pausar_cancion()
        if i == 10:
            i = 0
            print('musica anterior: {}'.format(objeto.listas_contenedor_de_song[objeto.indice_cancion]))
            objeto.indice_cancion += 1
            if j == tiempo_total_c:
                objeto.indice_cancion = 0

end = False
while not end:
    menum()
    r = input('Seeccion:')
    if r == '1':
        while True:
            comando_r(My_musica)
            print('Musica reproducida')
            r = input('Volver a R:(si)')
            if r == 'no':
                break
            
                
    if r == '0':
        break
