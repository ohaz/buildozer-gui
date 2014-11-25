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
        scrmgr.switch_to(scrmgr.get_screen('createproject'))

    def load_button_press(self):
        scrmgr.switch_to(scrmgr.get_screen('loadproject'))

class CreateProject(Screen):

    def back(self):
        scrmgr.switch_to(scrmgr.last_screen)

    def home(self):
        scrmgr.switch_to(scrmgr.get_screen('mainmenu'))

    def create_button_press(self):
        cur_dir = os.getcwd()
        title = self.ids.create_project_title.text
        package_name = self.ids.create_project_package.text
        domain = self.ids.create_project_domain.text
        landscape = self.ids.create_project_landscape.state
        all = self.ids.create_project_all.state
        orientation = 'portrait'
        if all == 'down':
            orientation = 'all'
        elif landscape == 'down':
            orientation = 'landscape'
        specparser.init_default_spec(cur_dir, orientation, domain, package_name, title)
        specparser.save_spec(cur_dir)
        scrmgr.switch_to(scrmgr.get_screen('loadproject'))

class LoadProject(Screen):
    def on_enter(self, *args):
        specparser.load_spec(os.getcwd())
        self.ids.load_project_title.text = 'Project: [b]'+specparser.get_title()+'[/b]'

    def compile_button_press(self):
        scrmgr.switch_to(scrmgr.get_screen('compileproject'))

    def edit_button_press(self):
        scrmgr.switch_to(scrmgr.get_screen('editproject'))

    def back(self):
        scrmgr.switch_to(scrmgr.last_screen)

    def home(self):
        scrmgr.switch_to(scrmgr.get_screen('mainmenu'))


class CompileProject(Screen):

    def back(self):
        scrmgr.switch_to(scrmgr.last_screen)

    def home(self):
        scrmgr.switch_to(scrmgr.get_screen('mainmenu'))


    @mainthread
    def set_compile_status(self, status):
        label = self.ids.compile_project_label
        if status == 1:
            label.color = (1,1,0,1)
            label.text = 'Compiling'
        elif status == 2:
            label.color = (0,1,0,1)
            label.text = 'Compiled successfully'
        else:
            label.color = (1,0,0,1)
            label.text = 'Compilation error'


    def compile_button_press(self):
        self.set_compile_status(1)
        targets = []
        if self.ids.compile_target_android.state == 'down':
            targets.append('android')
        if self.ids.compile_target_ios.state == 'down':
            targets.append('ios')
        if self.ids.compile_target_windows.state == 'down':
            # TODO not in buildozer yet
            pass
        if self.ids.compile_target_linux.state == 'down':
            # TODO not in buildozer yet
            pass
        debug = self.ids.compile_debug
        release = self.ids.compile_release
        configuration = 'debug'
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
        if 'packaging done!' in output:
            self.set_compile_status(2)
        else:
            self.set_compile_status(-1)

class EditProject(Screen):
    def back(self):
        scrmgr.switch_to(scrmgr.last_screen)

    def home(self):
        scrmgr.switch_to(scrmgr.get_screen('mainmenu'))

    def switch_to(self, to):
        self.ids.screen_manager.current = to
        self.ids.current_sub_menu.text = to

    def on_pre_enter(self, *args):
        self.load_basic_settings()
        self.load_incexc_settings()

    def load_basic_settings(self):
        self.ids.basic_title.text = specparser.get_title()
        self.ids.basic_package.text = specparser.get_package_name()
        self.ids.basic_domain.text = specparser.get_package_domain()
        if specparser.get_orientation() == 'all':
            self.ids.basic_all.state = 'down'
        elif specparser.get_orientation() == 'landscape':
            self.ids.basic_landscape.state = 'down'
        else:
            self.ids.basic_portrait.state = 'down'
        if specparser.get_fullscreen() == 1:
            self.ids.basic_fullscreen.state = 'down'

    def load_incexc_settings(self):
        self.ids.inc_sourcedir.text = specparser.get_source_dir()
        self.ids.inc_inc_exts.text = specparser.get_source_include_exts()
        self.ids.inc_exc_exts.text = specparser.get_source_exclude_exts()
        self.ids.inc_exc_patterns.text = specparser.get_source_exclude_patterns()
        self.ids.inc_exc_dirs.text = specparser.get_source_exclude_dirs()
        self.ids.inc_app_reqs.text = specparser.get_requirements()
        self.ids.inc_garden_reqs.text = specparser.get_garden_requirements()
        self.ids.inc_presplash.text = specparser.get_presplash()
        self.ids.inc_icon.text = specparser.get_icon_filename()

    def save(self):
        specparser.set_title(self.ids.basic_title.text)
        specparser.set_package_name(self.ids.basic_package.text)
        specparser.set_package_domain(self.ids.basic_domain.text)
        landscape = self.ids.basic_landscape.state
        all = self.ids.basic_all.state
        orientation = 'portrait'
        if all == 'down':
            orientation = 'all'
        elif landscape == 'down':
            orientation = 'landscape'
        specparser.set_orientation(orientation)
        if self.ids.basic_fullscreen.state == 'down':
            specparser.set_fullscreen(1)
        else:
            specparser.set_fullscreen(0)
        self.ids.save_button.text = '[color=00ff00]Saved[/color]'
        Clock.schedule_interval(self.revert_save, 5)
        specparser.save_spec()

    def revert_save(self, dt):
        self.ids.save_button.text = 'Save'


