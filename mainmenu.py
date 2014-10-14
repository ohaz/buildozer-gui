from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock, mainthread
import specparser


from subprocess import Popen, PIPE
import threading
import os

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
        self.ids.load_project_title.text = 'Project: [b]'+specparser.get_title()+'[/b]'

    def compile_button_press(self):
        scrmgr.get_sm().switch_to(scrmgr.get_screen('compileproject'))

    def edit_button_press(self):
        pass

class CompileProject(Screen):

    @mainthread
    def set_compile_status(self, status):
        label = self.ids.compile_project_label
        if status == 1:
            label.color = (1,1,0,1)
            label.text = 'Compiling'
        if status == 2:
            label.color = (0,1,0,1)
            label.text = 'Compiled successfully'

    def compile_button_press(self):
        self.set_compile_status(1)
        targets = []
        if self.ids.compile_target_android.state == 'down':
            targets.append('android')
        if self.ids.compile_target_ios.state == 'down':
            # TODO
            pass
        if self.ids.compile_target_windows.state == 'down':
            # TODO not in buildozer yet
            pass
        if self.ids.compile_target_linux.state == 'down':
            # TODO not in buildozer yet
            pass
        debug = self.ids.compile_debug
        release = self.ids.compile_release
        if debug.state == 'down':
            configuration = 'debug'
        elif release.state == 'down':
            configuration = 'release'
        settings = []
        if self.ids.compile_deploy.state == 'down':
            settings.append('deploy')
        if self.ids.compile_run.state == 'down':
            settings.append('run')
        threading.Thread(target=self.build, args=(targets, configuration, settings)).start()

    def build(self, targets, configuration, settings):
        cmd = ['buildozer']
        for t in targets:
            cmd.append(t)
        cmd.append(configuration)
        for s in settings:
            cmd.append(s)
        process = Popen(cmd, stdout=PIPE)
        (output,err) = process.communicate()
        exit_code = process.wait()
        self.set_compile_status(2)