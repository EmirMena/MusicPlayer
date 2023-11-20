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
    def load_playlist_GUI(self): #Cargar la lista de reproducción en la GUI
        actual_playlist = self.music_player.get_playlist_data()
        self.GUI.set_playlist(actual_playlist)
    def play_song(self):
        self.music_player.play_audio()   
        self.GUI.set_song_state("playing")
        self.GUI.generate_player_buttons()
    def pause_song(self):
        self.music_player.pause_audio()
        self.GUI.set_song_state("paused")
        self.GUI.generate_player_buttons()
    def unpause_song(self):
        self.music_player.unpause_audio()
        self.GUI.set_song_state("playing")
        self.GUI.generate_player_buttons()
    def next_song(self):
        self.music_player.next_song()
        self.GUI.set_song_state("playing")
        self.GUI.generate_player_buttons()
    def play_raw_song(self,song_path):#Reproducir cancion elegida en la GUI
        self.music_player.play_raw_audio(song_path)
        self.GUI.set_song_state("playing")
        self.GUI.generate_player_buttons()
    def add_song(self,song_name,autor,song_path):#añade cancion a la lista de reproduccion
        song_data=(song_name,autor)
        self.music_player.add_song_playlist_path(song_path)
        self.music_player.add_song_playlist_data(song_data)
        self.load_playlist_GUI()

        

    