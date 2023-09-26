import pygame

class MP3_Player():

    def __init__(self):
        pygame.mixer.init()
        self.reproduction_list = []  # Lista que actúa como la cola de reproducción
        self.actual_song_index = 0  # Índice de la canción actual en la lista de reproducción

    def play_audio(self):
        "musica sonando"
        pygame.mixer.music.stop()
        if not pygame.mixer.music.get_busy() and self.reproduction_list:
            pygame.mixer.music.load(self.reproduction_list[self.actual_song_index])
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
        print("Indice de reproduccón actual: " + str(self.actual_song_index) + " Longitud del array: " + str(len(self.reproduction_list)) + " Cancion: " + self.reproduction_list[0])
        print("Next song played: " + self.reproduction_list[self.actual_song_index])
        self.play_audio()
        if self.actual_song_index < len(self.reproduction_list):
            self.actual_song_index = self.actual_song_index + 1

    def add_song(self, song_path):
        if song_path:
            print("Added: " + song_path)
            self.reproduction_list.append(song_path)

    def song_is_playing(self):
        return pygame.mixer.music.get_busy()
    def get_actual_song_index(self):
        return self.actual_song_index
    
                        