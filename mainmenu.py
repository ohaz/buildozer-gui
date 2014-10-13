from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os
import specparser

from subprocess import Popen, PIPE

import scrmgr

Builder.load_file('mainmenu.kv')

class Mainmenu(Screen):

    def new_button_press(self):
        scrmgr.get_sm().switch_to(scrmgr.get_screen('createproject'))

    def load_button_press(self):
        scrmgr.get_sm().switch_to(scrmgr.get_screen('loadproject'))

class CreateProject(Screen):

    def create_button_press(self):
        cur_dir = os.getcwd()
        title = self.ids.create_project_title.text
        package_name = self.ids.create_project_package.text
        domain = self.ids.create_project_domain.text
        landscape = self.ids.create_project_landscape.state
        orientation = 'portrait'
        if landscape == 'down':
            orientation = 'landscape'
        specparser.init_default_spec(cur_dir, orientation, domain, package_name, title)
        specparser.save_spec(cur_dir)
        scrmgr.get_sm().switch_to(scrmgr.get_screen('loadproject'))

class LoadProject(Screen):
    def on_enter(self, *args):
        specparser.load_spec(os.getcwd())
        self.ids.load_project_title.text = specparser.get_title()
    def compile_button_press(self):
        process = Popen(["buildozer", "android", "debug"], stdout=PIPE)
        (output,err) = process.communicate()
        exit_code = process.wait()
    def edit_button_press(self):
        pass