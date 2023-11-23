import pygame
from models.Song import Song

class MP3_Player():

    def __init__(self):
        pygame.mixer.init()
        self.play_queue = []  # Lista que actúa como la cola de reproducción
        self.actual_song_index = 0  # Índice de la canción actual en la lista de reproducción

    def play_audio(self):
        "musica sonando"
        pygame.mixer.music.stop()
        if not pygame.mixer.music.get_busy() and self.play_queue:
            pygame.mixer.music.load(self.play_queue[self.actual_song_index].path)
            pygame.mixer.music.play()

    def play_raw_audio(self, song):
        pygame.mixer.music.stop()

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(song.path)
            pygame.mixer.music.play()

    def pause_audio(self):
        "Musica pausada"
        pygame.mixer.music.pause()

    def unpause_audio(self):
        "Musica Despausada"
        pygame.mixer.music.unpause()
    
    def rewind_audio(self):
        "Musica reiniciada"
        pygame.mixer.music.rewind()

    def next_song(self):
        self.play_audio()
        if self.actual_song_index < len(self.play_queue):
            self.actual_song_index = self.actual_song_index + 1

    def add_song_to_play_queue(self, song):
        if song:
            self.play_queue.append(song)
    def song_is_playing(self):
        return pygame.mixer.music.get_busy()
    def get_actual_song_index(self):
        return self.actual_song_index
    def get_play_queue(self):
        return self.play_queue
    
                        