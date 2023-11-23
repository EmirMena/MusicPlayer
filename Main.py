from GUI import GUI
from Music_Player_Controller import Music_Player_Controller

window = GUI()
Music_Player_Controller = Music_Player_Controller(window)
window.setController(Music_Player_Controller)
window.main_playback_window()

