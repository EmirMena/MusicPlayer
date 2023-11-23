from models.Song_List_Generator import Song_List_Generator
from Music_List_Reader import Music_List_Reader
from models.AVLTree_Name import AVLTree_Name
from models.AVLTree_Author import AVLTree_Author
from models.AVLTree_Genre import AVLTree_Genre

music_data = Music_List_Reader().read_file()
song_list = Song_List_Generator().generate_song_list(music_data)


def generar_arbol_autores():
        if len(song_list)==0: print('La lista está vacía')
        else:
            for song in song_list:
                if song.name != "Monaco": 
                    arbol_autores.insert(song)

def generar_arbol_nombres():
        if len(song_list)==0: print('La lista está vacía')
        else:
            for song in song_list:
                if song.name != "Monaco": 
                    arbol_nombres.insert(song)

def generar_arbol_generos():
        if len(song_list)==0: print('La lista está vacía')
        else:
            for song in song_list:
                if song.name != "Monaco": 
                    arbol_generos.insert(song)

arbol_nombres = AVLTree_Name(song_list[0])
arbol_generos = AVLTree_Genre(song_list[0])
arbol_autores = AVLTree_Author(song_list[0])
generar_arbol_nombres()
generar_arbol_generos()
generar_arbol_autores()
ascending_list = arbol_nombres.generate_ascending_list()
for song in ascending_list:
    print("Nombre: " + song.name + " " + "Genero: " + song.genre )

#print(arbol_generos.search_genre("Metal"))
"""print("\n")
for song in descending_list:
    print("Nombre: " + song.name)"""
