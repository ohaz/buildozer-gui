from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

import scrmgr

Builder.load_file('mainmenu.kv')

class Mainmenu(Screen):

    def new_button_press(self):
        scrmgr.get_sm().switch_to(scrmgr.get_screen('createproject'))

    def load_button_press(self):
        pass

class CreateProject(Screen):
    pass