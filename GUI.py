import customtkinter as ctk
from PIL import ImageTk, Image

class GUI:
    def __init__(self):

        self.window=None
        #atributos de despliegue
        self.song_list=[]
        self.song_is_playing=False
        #atributos de configuracion gráfica
        self.title_color="#55BDED"
        self.background_color="#362836"
        self.subtitle_color="#6298D2"
        self.main_text_color="#D95588"
        self.emphasis_color="#55BDED"
        self.secundary_background_color="#5E5A91"
        self.button_color="#533D5A"
        self.main_font="SquareFont"
        self.secundary_font="Dubai"

    def generate_window(self,titulo):
        self.window=ctk.CTk() #Se crea la ventana
        self.window.geometry("1280x720") #Se establece el tamaño
        self.window.title(titulo)#titulo de la ventana
        self.main_font = ctk.CTkFont(family=self.main_font, size=55)
        self.secundary_font = ctk.CTkFont(family=self.secundary_font, size=25)
        self.frame = ctk.CTkFrame(master=self.window, fg_color=self.background_color)
        self.frame.pack(pady=10, padx=10, fill="both", expand=True)
        self.label = ctk.CTkLabel(
            master=self.frame,
            text=titulo, 
            font=self.main_font, 
            bg_color=self.background_color, 
            text_color=self.title_color)
        self.label.pack(pady=0, padx=0)
        
    def main_playback_window(self):
        if self.window != None:
            self.window.destroy()
        self.generate_window("Reproductor")

        #Buscador de canciones y filtro (para la insercion)
        finder_frame = ctk.CTkFrame(master=self.frame)
        finder_frame.pack(pady=0, padx=0)
        search_entry_field=ctk.CTkEntry(
            master=finder_frame,
            fg_color=self.button_color,
            width=550,placeholder_text="Ingresar",
            font=self.secundary_font,border_width=0,
            corner_radius=0)
        search_entry_field.pack(side="left",pady=0,padx=0)

        #filtro de opciones
        option_frame = ctk.CTkFrame(master=self.frame, fg_color=self.background_color)
        option_frame.pack(side="top",ipadx=350)
        self.generate_option_menu(option_frame)

        #Generar los botones en la song_list_frame
        song_list_frame = ctk.CTkFrame(master=self.frame, fg_color=self.emphasis_color)
        song_list_frame.pack(pady=0, padx=0)
        self.generate_song_buttons(song_list_frame)
        
        #Generar la lista de reproduccion (canciones que sonarán)
        #reproduction_list_frame = ctk.CTkFrame(master=self.frame, fg_color=self.emphasis_color)
        #reproduction_list_frame.pack(pady=0, padx=0)
        #self.generate_repopduction_list(reproduction_list_frame)

        #Reproductor de musica (botones de play, next, previous?)
        player_frame = ctk.CTkFrame(
            master=self.window
            )
        player_frame.pack(pady=20, padx=0, side="bottom")
        self.generate_player_buttons(player_frame)

        
        self.window.mainloop()

        #FUNCIONES PARA GENERAR LOS BOTONES------------------------------------------------------------------
    def generate_reproduction_list(self,frame):
        for song in self.reproduction_list:
            songs_name, autor, song_path = song[0], song[1], song[3]
            reproduction_song_button =ctk.CTkButton(
                master=frame,
                text=songs_name + " from: " + autor,
                width=30, height=20,
                fg_color=self.secundary_background_color,
                bg_color=self.secundary_background_color,hover_color=self.title_color,
                font=self.secundary_font,
                corner_radius=0,
            )
            reproduction_song_button.grid(row_counter =+ 1)

    def generate_song_buttons(self,frame):
        BUTTON_WITDH = 690  # Ancho fijo para los botones
        BUTTON_HEIGHT = 35  # Alto fijo para los botones
        row_counter = 0
        add_icon = ctk.CTkImage(Image.open("MusicPlayer/images/add_icon.png"), size=(15, 15))
        scroller_frame=ctk.CTkScrollableFrame(
            master=frame,
            width=BUTTON_WITDH*1.2, height=BUTTON_HEIGHT*12.5,
            scrollbar_button_color=self.secundary_background_color,
            scrollbar_button_hover_color=self.emphasis_color,
            corner_radius=0
            )
        scroller_frame.pack(pady=0,padx=0)
        for song in self.song_list:
            songs_name, autor, song_path = song[0], song[1], song[3]
            reproduction_song_button =ctk.CTkButton(
                master=scroller_frame,
                text=songs_name + " from: " + autor,
                width=BUTTON_WITDH, height=BUTTON_HEIGHT,
                fg_color=self.secundary_background_color,
                bg_color=self.secundary_background_color,hover_color=self.title_color,
                font=self.secundary_font,
                corner_radius=0,
                command=lambda path=song_path: self.Music_Player_Controller.play_raw_song(path))
            reproduction_song_button.grid(row=row_counter + 1, column=0)
            add_song_button = ctk.CTkButton(
                master=scroller_frame, image=add_icon,
                text="", height=BUTTON_HEIGHT+13,
                fg_color=self.button_color,
                bg_color=self.button_color,hover_color=self.subtitle_color,
                font=self.secundary_font,
                corner_radius=0,
                command=lambda path=song_path: self.Music_Player_Controller.add_song(path))
            add_song_button.grid(row=row_counter + 1, column=1)
            row_counter += 1

    def generate_player_buttons(self,frame):
        BUTTON_WITDH = 40  # Ancho fijo para los botones
        BUTTON_HEIGHT = 40  # Alto fijo para los botones
        #boton de play y pausa (ya que ambos son los mismos)--------------------------------
        play_icon = ctk.CTkImage(Image.open("MusicPlayer/images/play_icon.png"), size=(BUTTON_WITDH, BUTTON_HEIGHT))
        pause_icon = ctk.CTkImage(Image.open("MusicPlayer/images/pause_icon.png"), size=(BUTTON_WITDH, BUTTON_HEIGHT))
        
        if self.song_is_playing:
            self.set_song_is_playing(False)
            pause_button = ctk.CTkButton(
                master=frame, image=pause_icon,
                fg_color=self.button_color, 
                bg_color="transparent", hover_color=self.subtitle_color,text="",
                corner_radius=0,
                compound="top",
                command=lambda: self.Music_Player_Controller.pause_song()
                )
            pause_button.pack(side="left", padx=0)
        else:
            self.set_song_is_playing(True)
            play_button = ctk.CTkButton(
                master=frame, image=play_icon,
                fg_color=self.button_color, 
                bg_color="transparent", hover_color=self.subtitle_color,text="",
                corner_radius=0,
                compound="top",
                command=lambda: self.Music_Player_Controller.play_song()
                )
            play_button.pack(side="left", padx=0)


        #boton de next----------------------------------
        next_icon=ctk.CTkImage(Image.open("MusicPlayer/images/next_icon.png"), size=(BUTTON_WITDH, BUTTON_HEIGHT))
        next_icon = ctk.CTkButton(
            master=frame, image=next_icon,
            fg_color=self.button_color, 
            bg_color="transparent", hover_color=self.subtitle_color,text="",
            corner_radius=0,
            compound="top",
            command=lambda: self.Music_Player_Controller.next_song()
            )
        next_icon.pack(side="right", padx=0)

    def generate_option_menu(self,frame): 
        #optionmenu_var = ctk.StringVar(value="option 3")
        optionmenu = ctk.CTkOptionMenu(
            master=frame,
            values=["Nombre", "Artista","Genero"],
            fg_color=self.main_text_color,
            bg_color="transparent",
            button_color=self.subtitle_color,
            button_hover_color=self.emphasis_color,
            corner_radius=0,
            height=45,
        )
        optionmenu.pack(side="right")

    def setController(self, Music_Player_Controller):
        self.Music_Player_Controller=Music_Player_Controller
    def set_song_is_playing(self,song_is_playing):
        self.song_is_playing=song_is_playing
    def set_song_list(self,song_list):
        self.song_list=song_list