from MP3_Player import MP3_Player
from Song_Searcher import Song_Searcher
from Music_List_Reader import Music_List_Reader
from GUI import GUI


class Music_Player_Controller():
    def __init__(self,GUI):
        self.GUI=GUI
        self.music_player = MP3_Player()
        self.song_searcher=Song_Searcher()
        self.load_play_queue_to_GUI()
        self.show_default_playlist()
        
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
    def rewind_song(self):
        self.music_player.rewind_audio()
        self.GUI.set_song_state("playing")
        self.GUI.generate_player_buttons()
    def play_raw_song(self,song):#Reproducir cancion elegida en la GUI
        self.music_player.play_raw_audio(song)
        self.GUI.set_song_state("playing")
        self.GUI.generate_player_buttons()
    def add_song(self,song):#añade cancion a la lista de reproduccion
        self.music_player.add_song_to_play_queue(song)
        self.load_play_queue_to_GUI()
    def search_songs(self,entry_values):
        #NOMBRE
        if (entry_values[0]!="" and entry_values[1]=="" and entry_values[2] ==""):
            self.show_song_by_name(entry_values[0])
        #GÉNERO
        elif (entry_values[1]!="" and entry_values[0]=="" and entry_values[2] ==""):
            self.show_song_by_genre(entry_values[1])
        #ARTISTA
        elif (entry_values[2]!="" and entry_values[0]=="" and entry_values[1] ==""):
            self.show_song_by_author(entry_values[2])
        
        #Nombre y Genero
        elif (entry_values[0]!="" and entry_values[1]!="" and entry_values[2] ==""):
            self.show_song_by_name_and_genre(entry_values[1])
        #Nombre y Artista
        elif (entry_values[0]!="" and entry_values[2]!="" and entry_values[1] ==""):
            self.show_song_by_name_and_author(entry_values[0],entry_values[2])
        #Artista y genero
        elif (entry_values[1]!="" and entry_values[2]!="" and entry_values[0] ==""):
            self.show_song_by_genre_and_author(entry_values[1], entry_values[2])
        #Nombre Artista Genero
        elif (entry_values[1]!="" and entry_values[2]!="" and entry_values[0] !=""):
            self.show_song_by_name_and_genre_author(entry_values[0], entry_values[1], entry_values[2] )

        self.GUI.refresh_main_playback_window()
#---------------------------------------------------------------------------
    def show_default_playlist(self): #Cargar canciones para mostrarlas en la GUI
        self.GUI.set_song_list(self.song_searcher.generate_default_list())
    def show_name_ascending_playlist(self):
        self.GUI.set_song_list(self.song_searcher.generate_name_ascending_list())
    def show_name_descending_playlist(self):
        self.GUI.set_song_list(self.song_searcher.generate_name_descending_list())
    def show_genre_ascending_playlist(self):
        self.GUI.set_song_list(self.song_searcher.generate_genre_ascending_list())
    def show_genre_descending_playlist(self):
        self.GUI.set_song_list(self.song_searcher.generate_genre_descending_list())
    def show_author_ascending_playlist(self):
        self.GUI.set_song_list(self.song_searcher.generate_author_ascending_list())
    def show_author_descending_playlist(self):
        self.GUI.set_song_list(self.song_searcher.generate_author_descending_list())
#-------------------------------------------------------------------------
    def show_song_by_name(self,name):
        self.GUI.set_song_list(self.song_searcher.search_song_by_name(name))
    def show_song_by_genre(self,genre):
        self.GUI.set_song_list(self.song_searcher.search_song_by_genre(genre))
    def show_song_by_author(self,author):
        self.GUI.set_song_list(self.song_searcher.search_song_by_author(author))
    def show_song_by_name_and_genre(self,name,genre):
        self.GUI.set_song_list(self.song_searcher.search_song_by_name_and_genre(name,genre))
    def show_song_by_genre_and_author(self,genre,author):
        self.GUI.set_song_list(self.song_searcher.search_song_by_genre_and_author(genre,author))
    def show_song_by_name_and_genre_author(self,name,genre,author):
        self.GUI.set_song_list(self.song_searcher.search_song_by_name(name))
    def show_song_by_name_and_author(self,name, author):
        print(name+author)
        self.GUI.set_song_list(self.song_searcher.search_song_by_name_and_author(name, author))
#---------------------------------------------------------------------------------------
    def load_play_queue_to_GUI(self): #Cargar la lista de reproducción en la GUI
        self.GUI.play_queue = self.music_player.get_play_queue()
    def refresh_GUI_by_order(self,order_choice):
        if (order_choice=="Nombre"):
            self.show_name_ascending_playlist()
        elif (order_choice=="Nombre (descendiente)"):
            self.show_name_descending_playlist()
        elif (order_choice=="Artista"):
            self.show_author_ascending_playlist()
        elif (order_choice=="Artista (descendiente)"):
            self.show_author_descending_playlist()
        elif (order_choice=="Género"):
            self.show_genre_ascending_playlist()
        elif (order_choice=="Género (descendiente)"):
            self.show_genre_descending_playlist()
        self.GUI.refresh_main_playback_window()
    