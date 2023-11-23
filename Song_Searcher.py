from models.Song_List_Generator import Song_List_Generator
from Music_List_Reader import Music_List_Reader
from models.Song import Song
from models.AVLTree_Name import AVLTree_Name
from models.AVLTree_Author import AVLTree_Author
from models.AVLTree_Genre import AVLTree_Genre

class Song_Searcher:
    def __init__(self):
        self.music_data = Music_List_Reader().read_file()
        self.song_list = Song_List_Generator().generate_song_list(self.music_data)

        self.names_tree = AVLTree_Name(self.song_list[0])
        self.genres_tree = AVLTree_Genre(self.song_list[0])
        self.authors_tree = AVLTree_Author(self.song_list[0])

        self.__generate_trees()

#---------------------------------------------------Methods for filling the trees----------------------------
    def __generate_trees(self):
        self.__generate_names_tree()
        self.__generate_genres_tree()
        self.__generate_authors_tree()

    def __generate_names_tree(self):
        if len(self.song_list)==0: print('List is empty')
        else:
            for song in self.song_list:
                if song.name != "Monaco": 
                    self.names_tree.insert(song)
    
    def __generate_genres_tree(self):
        if len(self.song_list)==0: print('List is empty')
        else:
            for song in self.song_list:
                if song.name != "Monaco": 
                    self.genres_tree.insert(song)

    def __generate_authors_tree(self):
        if len(self.song_list)==0: print('List is empty')
        else:
            for song in self.song_list:
                if song.name != "Monaco": 
                    self.authors_tree.insert(song)
    
#---------------------------------------------------Listing methods---------------------------------------------------
    def generate_default_list(self):
        return self.song_list
    
    def generate_name_ascending_list(self):
        return self.names_tree.generate_ascending_list()

    def generate_name_descending_list(self):
        return self.names_tree.generate_descending_list()
    
    def generate_genre_ascending_list(self):
        return self.genres_tree.generate_ascending_list()
    
    def generate_genre_descending_list(self):
        return self.genres_tree.generate_descending_list()

    def generate_author_ascending_list(self):
        return self.authors_tree.generate_ascending_list()
    
    def generate_author_descending_list(self):
        return self.authors_tree.generate_descending_list()

#---------------------------------------------------Searching methods---------------------------------------------------
    def search_song_by_name(self, name):
        return self.song_to_list(self.names_tree.search_name(name))

    def search_song_by_genre(self, genre):
        return self.genres_tree.search_genre(genre)

    def search_song_by_author(self, author):
        return self.authors_tree.search_author(author)
    
    def search_song_by_name_and_genre(self, name: str, genre: str):
        song_searched_by_name = self.names_tree.search_name(name)
        genre_list = self.genres_tree.search_genre(genre)
        if((song_searched_by_name == None) or (genre_list == None)):
            return None
        else: 
            if (self.search_for_song_name_in_list(song_searched_by_name, genre_list) == True):
                return self.song_to_list(song_searched_by_name)
            else:
                return None
    
    def search_song_by_genre_and_name(self, genre:str, name:str):
        self.search_song_by_name_and_genre(name, genre)
            
    def search_song_by_name_and_author(self, name: str, author: str):
        song_searched_by_name = self.names_tree.search_name(name)
        author_list = self.authors_tree.search_author(author)
        if((song_searched_by_name == None) or (author_list == None)):
            return None
        else: 
            if (self.search_for_song_name_in_list(song_searched_by_name, author_list) == True):
                return self.song_to_list(song_searched_by_name)
            else:
                return None

    def search_song_by_author_and_name(self, author: str, name: str):
        self.search_song_by_name_and_author(name, author)

    def search_song_by_genre_and_author(self, genre: str, author: str):
        genre_list = self.genres_tree.search_genre(genre)
        author_list = self.authors_tree.search_author(author)
        if ((genre_list == None) or (author_list == None)):
            return None
        else:
            coincidences_list = self.search_coincidences_between_lists(genre_list, author_list)
            if (coincidences_list == None):
                return None
            else:
                return coincidences_list
            
    def search_song_by_author_and_genre(self, author: str, genre: str):
        self.search_song_by_genre_and_author(genre, author)

    def search_for_song_name_in_list(self, song_by_name: Song, genre_or_author_list: []):
        if len(genre_or_author_list) == 0: return False
        else:
            for song in genre_or_author_list:
                if(song_by_name.name == song.name):
                    return True
            return False
    
    def search_coincidences_between_lists(self, genre_list: [], author_list: []):
        coincidences_list = []
        for song in genre_list:
            for aux_song in author_list:
                if(song.name == aux_song.name):
                    coincidences_list.append(song)
        return coincidences_list
        
    def song_to_list(self,song):
        simple_list=[]
        simple_list.append(song)
        return simple_list




    