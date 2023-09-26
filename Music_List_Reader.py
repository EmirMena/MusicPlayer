class Music_List_Reader():
    def __init__(self):
        self.file_path = "Music_List.txt" 

    def read_file(self):
        data = []
        try:
            with open(self.file_path, 'r') as file:
                print(data)
                for line in file:
                    columns = line.strip().split(',')
                    if len(columns) == 4:
                        data.append(columns)
        except FileNotFoundError:
            print(f"El archivo {self.archivo} no fue encontrado.")
        return data







