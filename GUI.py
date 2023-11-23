import customtkinter as ctk
from PIL import ImageTk, Image

class GUI:
    def __init__(self):
        #atributos de despliegue
        ctk.set_appearance_mode("dark")
        self.window=None
        self.song_list=[]
        self.playlist=[]
        self.song_state="stopped"
        self.title=""

#VENTANAS-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    def generate_window(self,titulo):
        self.titulo=titulo
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

        self.window=ctk.CTk() 
        self.window.geometry("1280x720")
        self.window.title(titulo)
        self.main_font = ctk.CTkFont(family=self.main_font, size=55)
        self.secundary_font = ctk.CTkFont(family=self.secundary_font, size=25)
        self.frame = ctk.CTkFrame(master=self.window, fg_color=self.background_color)
        self.frame.pack(pady=10, padx=10, fill="both", expand=True)
        self.label = ctk.CTkLabel(
            master=self.frame,
            text=self.titulo, 
            font=self.main_font, 
            bg_color=self.background_color, 
            text_color=self.title_color)
        self.label.pack(pady=0, padx=0)
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #VENTANA PRINCIPAL
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def main_playback_window(self):
        if self.window != None:
            self.window.destroy()
        self.generate_window("Reproductor")

        #Buscador de canciones y filtro (para la insercion)
        finder_frame = ctk.CTkFrame(master=self.frame)
        finder_frame.pack(pady=0, padx=0)
        self.generate_search_entry_field(finder_frame,"left","Cancion")
        self.generate_search_entry_field(finder_frame,"right","Artista")

        #filtro de opciones
        option_frame = ctk.CTkFrame(master=self.frame, fg_color=self.background_color)
        option_frame.pack(side="top",ipadx=350)
        self.generate_option_menu(option_frame)

        #Generar los botones en la song_list_frame
        self.song_list_frame = ctk.CTkFrame(master=self.frame, fg_color=self.emphasis_color)
        self.song_list_frame.pack(pady=0, padx=0)
        self.generate_song_buttons()
        
        #Reproductor de musica (botones de play, next, previous?)
        control_bar_frame = ctk.CTkFrame(master=self.window,fg_color="transparent")
        control_bar_frame.pack(pady=20, side="bottom")
        self.player_frame = ctk.CTkFrame(master=control_bar_frame)
        self.player_frame.pack(pady=0, padx=340, side="left")
        self.generate_player_buttons()
        playlist_button_frame= ctk.CTkFrame(master=control_bar_frame)
        playlist_button_frame.pack(pady=0, padx=0, side="right")
        self.generate_button(playlist_button_frame,"MusicPlayer/images/playlist_icon.png",self.playlist_window,"right")

        self.window.mainloop()
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    VENTANA LISTA DE REPRODUCCION
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def playlist_window(self):
        if self.window != None:
            self.window.destroy()
        self.generate_window("Reproductor")
        playlist_frame=ctk.CTkFrame(master=self.frame)
        playlist_frame.pack(side="top")
        self.generate_playlist_songs(playlist_frame)

        control_bar_frame = ctk.CTkFrame(master=self.window,fg_color="transparent")
        control_bar_frame.pack(pady=20, side="bottom")
        self.player_frame = ctk.CTkFrame(master=control_bar_frame)
        self.player_frame.pack(pady=0, padx=340, side="left")
        self.generate_player_buttons()
        music_player_button_frame= ctk.CTkFrame(master=control_bar_frame)
        music_player_button_frame.pack(pady=0, padx=0, side="right")
        self.generate_button(music_player_button_frame,"MusicPlayer/images/music_player_icon.png",self.main_playback_window,"right")
        self.window.mainloop()

    """FUNCIONES PARA GENERAR LOS BOTONES------------------------------------------------------------------------------------------------------------------------"""
    def generate_playlist_songs(self,frame):
        BUTTON_WITDH = 690  # Ancho fijo para los botones
        BUTTON_HEIGHT = 35  # Alto fijo para los botones
        row_counter = 0
        scroller_frame=ctk.CTkScrollableFrame(
            master=frame,
            width=BUTTON_WITDH, height=BUTTON_HEIGHT*15,
            scrollbar_button_color=self.secundary_background_color,
            scrollbar_button_hover_color=self.emphasis_color,
            corner_radius=0
            )
        scroller_frame.pack(pady=0,padx=0)
        print(self.playlist)
        for song in self.playlist:
            songs_name, autor = song[0], song[1]
            playlist_song_button =ctk.CTkButton(
                master=scroller_frame,
                text=songs_name + " from: " + autor,
                width=BUTTON_WITDH, height=BUTTON_HEIGHT,
                fg_color=self.secundary_background_color,
                bg_color=self.secundary_background_color,hover_color=self.title_color,
                font=self.secundary_font,
                corner_radius=0,
            )
            playlist_song_button.grid(row=row_counter + 1, column=1)
            row_counter += 1

    def generate_song_buttons(self):
        for widget in self.song_list_frame.winfo_children():
            widget.destroy()
        BUTTON_WITDH = 690  # Ancho fijo para los botones
        BUTTON_HEIGHT = 35  # Alto fijo para los botones
        row_counter = 0
        add_icon = ctk.CTkImage(Image.open("MusicPlayer/images/add_icon.png"), size=(15, 15))
        scroller_frame=ctk.CTkScrollableFrame(
            master=self.song_list_frame,
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
                command=lambda song_name=songs_name,autor=autor, path=song_path: self.Music_Player_Controller.add_song(song_name,autor,path))
            add_song_button.grid(row=row_counter + 1, column=1)
            row_counter += 1

    def generate_player_buttons(self):
        for widget in self.player_frame.winfo_children():
            widget.destroy()
        # Botón de previous, que funciona para reiniciar la canción
        self.generate_button(
            self.player_frame,
            "MusicPlayer/images/previous_icon.png",
            self.rewind_song_command_request,
            "left"
        )
        # Botón de play y pausa (ya que ambos son los mismos)
        if self.song_state == "playing":
            self.generate_button(
                self.player_frame,
                "MusicPlayer/images/pause_icon.png",
                self.pause_song_command_request,
                "left"
        )
        elif self.song_state == "stopped" or self.song_state == "paused":
            self.generate_button(
                self.player_frame,
                "MusicPlayer/images/play_icon.png",
                self.play_song_command_request if self.song_state == "stopped" else self.unpause_song_command_request,
                "left"
        )
        # Botón de next
        self.generate_button(
            self.player_frame,
            "MusicPlayer/images/next_icon.png",
            self.next_song_command_request,
            "left"
        )

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

    def generate_button(self, frame, path, command, pack_side):
        BUTTON_WITDH = 40  # Ancho fijo para los botones
        BUTTON_HEIGHT = 40  # Alto fijo para los botones
        icon = ctk.CTkImage(Image.open(path), size=(BUTTON_WITDH, BUTTON_HEIGHT))
        icon = ctk.CTkButton(
            master=frame, image=icon,
            fg_color=self.button_color, 
            bg_color="transparent", hover_color=self.subtitle_color,text="",
            corner_radius=0,
            compound="top",
            command=lambda: command()
            )
        icon.pack(side=pack_side, padx=0)

    def generate_search_entry_field(self,frame,side,placeholder):
        #Buscador de canciones y filtro (para la insercion)
        search_entry_field=ctk.CTkEntry(
            master=frame,
            fg_color=self.button_color,
            width=350,placeholder_text=placeholder,
            font=self.secundary_font,border_width=0,
            corner_radius=0)
        search_entry_field.pack(side=side,pady=0,padx=2)

    """GETTERS Y SETTERS---------------------------------------------------------------------------------------------------------------------------- """
    def setController(self, Music_Player_Controller):
        self.Music_Player_Controller=Music_Player_Controller
    def set_song_state(self,song_state):
        self.song_state=song_state
        print(self.song_state)
    def set_song_list(self,song_list):
        self.song_list=song_list
    def set_playlist(self,playlist):
        self.playlist=playlist
    def play_song_command_request(self):
        self.Music_Player_Controller.play_song()
    def pause_song_command_request(self):
        self.Music_Player_Controller.pause_song()
    def play_song_command_request(self):
        self.Music_Player_Controller.play_song()
    def unpause_song_command_request(self):
        self.Music_Player_Controller.unpause_song()
    def next_song_command_request(self):
        self.Music_Player_Controller.next_song()
    def rewind_song_command_request(self):
        self.Music_Player_Controller.rewind_song()