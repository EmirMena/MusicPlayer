class Music_List_Reader():
    def __init__(self):
        self.file_path = "MusicPlayer/Music_List.txt" 

    def read_file(self):
        music_data = []
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    columns = line.strip().split(',')
                    if len(columns) == 4:
                        music_data.append(columns)
        except FileNotFoundError:
            print(f"El archivo {self.file_path} no fue encontrado.")
        return music_data







