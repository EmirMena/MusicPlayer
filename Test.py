from models.Song_List_Generator import Song_List_Generator
from Music_List_Reader import Music_List_Reader
from models.AVLTree_Name import AVLTree_Name
from models.AVLTree_Author import AVLTree_Author

music_data = Music_List_Reader().read_file()
song_list = Song_List_Generator().generate_song_list(music_data)

def generar_arbol_nombres():
        if len(song_list)==0: print('La lista está vacía')
        else:
            for song in song_list:
                if song.name == "Monaco": pass
                arbol_nombres.insert(song)

def generar_arbol_autores():
        if len(song_list)==0: print('La lista está vacía')
        else:
            for song in song_list:
                if song.name == "Monaco": pass
                arbol_autores.insert(song)

arbol_nombres = AVLTree_Name(song_list[0])
arbol_autores = AVLTree_Author(song_list[0])
generar_arbol_nombres()
ascending_list = arbol_nombres.generate_ascending_list()
descending_list = arbol_nombres.generate_descending_list()
for song in ascending_list:
    print("Nombre: " + song.name)
print("\n")
for song in descending_list:
    print("Nombre: " + song.name)
