import pygame

class MP3_Player():

    def __init__(self):
        pygame.mixer.init()
        self.playlist_path = []  # Lista que actúa como la cola de reproducción
        self.actual_song_index = 0  # Índice de la canción actual en la lista de reproducción
        self.playlist_data = [] #Lista que contiene nombre y autor de la cancion

    def play_audio(self):
        "musica sonando"
        pygame.mixer.music.stop()
        if not pygame.mixer.music.get_busy() and self.playlist_path:
            pygame.mixer.music.load(self.playlist_path[self.actual_song_index])
            pygame.mixer.music.play()

    def play_raw_audio(self, song_path):
        print("Played raw: " + song_path)
        pygame.mixer.music.stop()
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()

    def pause_audio(self):
        "Musica pausada"
        pygame.mixer.music.pause()

    def unpause_audio(self):
        "Musica Despausada"
        pygame.mixer.music.unpause()

    def next_song(self):
        print("Indice de reproduccón actual: " + str(self.actual_song_index) + " Longitud del array: " + str(len(self.playlist_path)) + " Cancion: " + self.playlist_path[0])
        print("Next song played: " + self.playlist_path[self.actual_song_index])
        self.play_audio()
        if self.actual_song_index < len(self.playlist_path):
            self.actual_song_index = self.actual_song_index + 1

    def add_song_playlist_path(self, song_path):
        if song_path:
            print("Added: " + song_path)
            self.playlist_path.append(song_path)

    def add_song_playlist_data(self,song_data):
        if song_data:
            self.playlist_data.append(song_data)
        

    def song_is_playing(self):
        return pygame.mixer.music.get_busy()
    def get_actual_song_index(self):
        return self.actual_song_index
    def get_playlist_path(self):
        return self.playlist_path
    def get_playlist_data(self):
        return self.playlist_data
    
                        