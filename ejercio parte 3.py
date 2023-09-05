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

    def Eliminar_cancion(self,index):                     #Un método que permitirá eliminar una canción.
        self.listas_contenedor_de_song.remove(self.listas_contenedor_de_song[index])       #eliminar una la cancion ,atraves de la funcion remove

    def Mostrar_Todas_las_canciones(self):                 # Un método que permitirá mostrar todas las canciones.
        for x in range(len(self.listas_contenedor_de_song)):
            print(x,'¬. ',self.listas_contenedor_de_song[x])

    def Comienza_Reproducir_cancion(self):                          # comienza a reproducir una canción
        self.Estado = 'Reproduciendo'
        return self.listas_contenedor_de_song[self.indice_cancion]
    
    def Seleccionar_una_cancion_a_reproducir(self,indice):
        self.indice_cancion = indice                           # Cambiar el valor de la actual reproducion y colocar ah reproducir el nuevo

    def Pausar_cancion(self):
        self.Estado = 'Pausado'
        print('La cancion se encuentra pausada')
        m = input('Enter para dejar la pausa')
        self.Estado = 'Reproduccion'
    def Detener_la_reproduccion(self):
        self.Estado = 'Detenido'
        print('La cancion se encuentra Detenida')
        m = input('Cancion Detenida (enter para volver a reproduccir cancion) ')
        self.Estado = 'Reproduccion'

    def Pasar_sig_cancion(self,ind_actual):
        if ind_actual < (len(self.listas_contenedor_de_song)-1):
            self.indice_cancion += 1
        else:
            self.indice_cancion = 0

        print('Siguiente...')
    def Retroceder_cancion_anterior(self,id_actual):
        if id_actual < (len(self.listas_contenedor_de_song)-1):
            self.indice_cancion -= 1
        else:
            self.indice_cancion = len(self.listas_contenedor_de_song)-1     
                                      
        print('Retrocediendo...')
    def Reproducir_una_cancion_aleatoria(self,index_actual = None):
        cancion_que_se_estaba_r = self.listas_contenedor_de_song[self.indice_cancion]     
        lista = self.listas_contenedor_de_song
        len_lista = len(self.listas_contenedor_de_song)
        i = 0
        while len(lista) > i:
            numero_aleatorio = rd.randrange(len_lista)
            aux = lista[i]
            lista[i] = lista[numero_aleatorio]
            lista[numero_aleatorio] = aux
            i += 1
        if index_actual != None:
            indice_cancion_que_se_estaba_r = lista.index(cancion_que_se_estaba_r)
            return indice_cancion_que_se_estaba_r 
    def Ver_estado_Playlist(self):
        return 'Esta playlist esta en {}'.format(self.Estado)      
    def Ver_cancion_reproduciendo(self):
        return f'La cancion que se esta REPRODUCIENDO es: {self.listas_contenedor_de_song[self.indice_cancion]}'
    #METODO PARA ELIMINAR OBJ
    def __del__(self):
        print('objeto destruido')

canciones = ['musica pop','musica clasica','musica jazz']
My_musica = Playlist('XXLL',canciones)
def Editar(opcion):
    if opcion == 'a':
       My_musica.Mostrar_Todas_las_canciones() 

    if opcion == 'b':
        index = int(input(f'Ingrese el numero de la cancion a eliminar(0-{len(My_musica.listas_contenedor_de_song)-1})(-1)Para Cancelar: '))
        if index > -1:
            My_musica.Eliminar_cancion(index)
            print('Canción Eliminada de tu Playlist')
        
    if opcion == 'c':
        nombre = input('Ingrese el nombre de la cancion: ')
        My_musica.Añadir_cancion(nombre)
        print('Cancion agregada en tu play list. En top {}'.format(len(My_musica.listas_contenedor_de_song)-1))
def comando_r(objeto):
    objeto.Estado = 'Reproduccion'
    tiempo_total_c = len(canciones) * 15
    i = j = 0
    TiempoC = 15
    while i < TiempoC and j <tiempo_total_c:
        c_id = Modo_aleatorio = None
        if keyboard.is_pressed('p'):                         # Al precionar la tecla p se pausara la playlist
            objeto.Pausar_cancion()
        if objeto.Estado == 'Reproduccion':
            if Modo_aleatorio == None:
                objeto.listas_contenedor_de_song[objeto.indice_cancion]
                time.sleep(1)
                print(i)
                i += 1
                j += 1
            elif Modo_aleatorio == True:    
                if c_id != objeto.indice_cancion:
                    objeto.listas_contenedor_de_song[objeto.indice_cancion]
                    time.sleep(1)
                    print(i)
                    i += 1
                    j += 1
                else:
                    j += TiempoC             # tiempo por cancion , cuando este en aleatoria la musica que se esta en R y se colo el modo Aletorio, este indice no se contara y se suma , para evitar que salga
                    continue

        if keyboard.is_pressed('p'):                        #comando para pausar
            objeto.Pausar_cancion()

        if keyboard.is_pressed('S'):                        # comando para seleccionar la cancion ah reproducir
           ingrese = int(input(f'Ingrese el numero de la cancion(0-{len(objeto.listas_contenedor_de_song)-1}): '))
           objeto.Seleccionar_una_cancion_a_reproducir(ingrese)
           i = 0
           j = 15*ingrese

        if keyboard.is_pressed('D'):  
           objeto.Detener_la_reproduccion()                     # comando para detener la reproducir
           i = 0
        if keyboard.is_pressed('N'):
            el_resto_song_actual = j % 15 #objeto.indice_cancion
            objeto.Pasar_sig_cancion(objeto.indice_cancion)
            i = 0
            j += el_resto_song_actual          # le sumamos lo que restaba del tiempo de la cancion anterior , para que la siguinete inicie con el tiempo 0 y que en la lista de tiempode demora total , se tenga el numero mazimo que se tiene.
        if keyboard.is_pressed('R'):           # comando para retroceder la cancion
            el_resto_song_actual = j % 15 #objeto.indice_cancion
            objeto.Retroceder_cancion_anterior(objeto.indice_cancion)
            i = 0
            j = (j + el_resto_song_actual)  -15        # se suma lo que llebaba y se resta los 15 , para que de el efeto de retornar , desde el punto de partica pero esta vez en 0

        if keyboard.is_pressed('9'):           # comando para ver el estado de la playlist. #agregar en los demas comando de pausa y detener
           print( objeto.Ver_estado_Playlist())
        if keyboard.is_pressed('V') or keyboard.is_pressed('v'):            # comado para ver la cancion actual
            print(objeto.Ver_cancion_reproduciendo())
        if keyboard.is_pressed('A'):
            r = input('Estas seguro de colocar la reproduccion aletoria? (si)(no): ')
            if r ==  'si':
                i = 0
                j += j%15           
                x =objeto.Reproducir_una_cancion_aleatoria(objeto.indice_cancion)
                c_id = x
                Modo_aleatorio = True
            else:
                continue
        if i == 15:
            i = 0
            print('musica anterior: {}'.format(objeto.listas_contenedor_de_song[objeto.indice_cancion]),objeto.indice_cancion)
            if objeto.indice_cancion < (len(objeto.listas_contenedor_de_song)-1 ):
                objeto.indice_cancion += 1
            if j == tiempo_total_c:
                objeto.indice_cancion = 0
    print(i,'--->', j)

def menu_de_reproduccion():
    print('---------------------------MENU DE COMNADO(TECLAS)--------------------------')
    print('Reproducccion ALEATORIA(A)|Pausar(P)|Detener(D)|Siguiente(N)|Retroceder(R)|')
    print("Seleccionar Song(S)|Estado(E) | Veer Song actual(V)\n")
end = False 
while not end:
    print('- '*40)
    print('--------BIENVENIDO. Para manejar tu Playlist tienes los siguiEntes opciones-----')
    print('\ta).mostrar todas las canciones.')
    print('\tb).Eliminar una canción.')
    print('\tc).añadir una canción')
    print('\td).Reproducir Playlist')
    print('\te).Reproducir Playlist Aleatoria')
    print('\tf).Salir')
    r = input('Ingrese una opcion:').lower()
    if r == 'a':
        Editar('a')
    if r == 'b':
        Editar('b')
    if r == 'c':
        Editar('c')
    if r == 'd':
        menu_de_reproduccion()
        while True:
            comando_r(My_musica)
            print('Musica reproducida')
            r = input('Volver a Reproducir:(si)')
            if r == 'no':
                break  
    if r == 'e':
        menu_de_reproduccion()
        My_musica.Reproducir_una_cancion_aleatoria()
        while True:
            comando_r(My_musica)
            print('Musica reproducida')
            r = input('Volver a Reproducir:(si)')
            if r == 'no':
                break
    if r == 'f':
        del My_musica
        break
