from models.Song_List_Generator import Song_List_Generator
from Music_List_Reader import Music_List_Reader
from models.AVLTree_Name import AVLTree_Name

music_data = Music_List_Reader().read_file()
song_list = Song_List_Generator().generate_song_list(music_data)

def generar_arbol_nombres():
        if len(song_list)==0: print('La lista está vacía')
        else:
            for song in song_list:
                if song.name == "Monaco": pass
                arbol_nombres.insert(song)

arbol_nombres = AVLTree_Name(song_list[0])
generar_arbol_nombres()
arbol_nombres.ascending_list()
arbol_nombres.descending_list()

