from models.Song import Song

class Song_List_Generator():

    def __init__(self):
        self.song_list = []

    def generate_song_list(self, music_data):
        for instance in music_data:
            self.song_list.append(Song(instance[0], instance[1], instance[2], instance[3]))
        return self.song_list