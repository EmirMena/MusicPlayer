from MP3_Player import MP3_Player
from Music_List_Reader import Music_List_Reader
from GUI import GUI

class Music_Player_Controller():
    def __init__(self,GUI):
        self.GUI=GUI
        self.music_player = MP3_Player()
        self.music_list_reader = Music_List_Reader() #se crea la instancia encargada del manejo de lectura
        self.song_list = self.music_list_reader.read_file() #se lee el archivo de las canciones y se almacena en una lista
        self.load_songs_GUI()
        
    def load_songs_GUI(self): #Cargar canciones para mostrarlas en la GUI
        self.GUI.set_song_list(self.song_list)
    def play_song(self):
        self.music_player.play_audio()
        #self.song_is_playing()

    def pause_song(self):
        self.music_player.pause_audio()
        #self.song_is_playing()
    def unpause_song(self):
        self.music_player.unpause_audio()
    def next_song(self):
        self.music_player.next_song()
    def play_raw_song(self,song_path):#Reproducir cancion elegida en la GUI
        self.music_player.play_raw_audio(song_path)
    def add_song(self,song_path):#añade cancion a la lista de reproduccion
        self.music_player.add_song(song_path)
    def song_is_playing(self):
        #comprobar si la cancion está sonando para cambiar la interfaz
        if self.music_player.song_is_playing():
            print("sonando")
            self.GUI.set_song_is_playing(True)
        else:
            print("pausada")
            self.GUI.set_song_is_playing(False)
        

        

    