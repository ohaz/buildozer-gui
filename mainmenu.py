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
        self.load_android_settings()
        self.load_ios_settings()
        self.load_other_settings()
        self.load_buildozer_settings()

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

    def load_android_settings(self):
        self.ids.android_permissions.text = specparser.get_android_permissions()
        self.ids.android_api.text = specparser.get_android_api_level()
        self.ids.android_minapi.text = specparser.get_android_min_api_level()
        self.ids.android_sdk.text = specparser.get_android_sdk()
        self.ids.android_ndk.text = specparser.get_android_ndk()
        self.ids.android_private_storage.text = specparser.get_android_use_private_storage()
        self.ids.android_ndk_path.text = specparser.get_android_ndk_path()
        self.ids.android_sdk_path.text = specparser.get_android_sdk_path()
        self.ids.android_p4a_path.text = specparser.get_android_p4a_path()
        self.ids.android_p4a_whitelist.text = specparser.get_android_p4a_whitelist()
        self.ids.android_p4a_branch.text = specparser.get_android_p4a_branch()
        self.ids.android_entrypoint.text = specparser.get_android_entrypoint()
        self.ids.android_add_jars.text = specparser.get_android_add_jars()
        self.ids.android_add_src.text = specparser.get_android_add_src()
        self.ids.android_ouya_category.text = specparser.get_android_ouya_category()
        self.ids.android_ouya_icon_filename.text = specparser.get_icon_filename()
        self.ids.android_manifest_intent_filters.text = specparser.get_android_manifest_intent_filters()
        self.ids.android_add_libraries_armeabi.text = specparser.get_android_add_libs_armeabi()
        self.ids.android_add_libraries_armeabi_v7a.text = specparser.get_android_add_libs_armeabi_v7a()
        self.ids.android_add_libraries_x86.text = specparser.get_android_add_libs_x86()
        self.ids.android_add_libraries_mips.text = specparser.get_android_add_libs_mips()
        self.ids.android_wakelock.text = specparser.get_android_wakelock()
        self.ids.android_meta_data.text = specparser.get_android_meta_data()
        self.ids.android_library_references.text = specparser.get_android_library_references()

    def load_ios_settings(self):
        self.ids.ios_codesign_debug.text = specparser.get_ios_codesign_debug()
        self.ids.ios_codesign_release.text = specparser.get_ios_codesign_release()

    def load_other_settings(self):
        #No other settings exist yet
        pass

    def load_buildozer_settings(self):
        self.ids.buildozer_loglevel.text = specparser.get_buildozer_log_level()
        self.ids.buildozer_warn_on_root.text = specparser.get_buildozer_warn_on_root()

    def save(self):
        self.save_basic_settings()
        self.save_incexc_settings()
        specparser.save_spec()
        self.ids.save_button.text = '[color=00ff00]Saved[/color]'
        Clock.schedule_interval(self.revert_save, 5)

    def save_basic_settings(self):
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

    def save_incexc_settings(self):
        specparser.set_source_dir(self.ids.inc_sourcedir.text)
        specparser.set_source_include_exts(self.ids.inc_inc_exts.text)
        specparser.set_source_exclude_dirs(self.ids.inc_exc_exts.text)
        specparser.set_source_exclude_patterns(self.ids.inc_exc_patterns.text)
        specparser.set_source_exclude_dirs(self.ids.inc_exc_dirs.text)
        specparser.set_requirements(self.ids.inc_app_reqs.text)
        specparser.set_garden_requirements(self.ids.inc_garden_reqs.text)
        specparser.set_presplash(self.ids.inc_presplash.text)
        specparser.set_icon_filename(self.ids.inc_icon.text)

    def save_android_settings(self):
        specparser.set_android_permissions(self.ids.android_permissions.text)
        specparser.set_android_api_level(self.ids.android_api.text)
        specparser.set_android_min_api_level(self.ids.android_minapi.text)
        specparser.set_android_sdk(self.ids.android_sdk.text)
        specparser.set_android_ndk(self.ids.android_ndk.text)
        specparser.set_android_use_private_storage(self.ids.android_private_storage.text)
        specparser.set_android_ndk_path(self.ids.android_ndk_path.text)
        specparser.set_android_sdk_path(self.ids.android_sdk_path.text)
        specparser.set_android_p4a_path(self.ids.android_p4a_path.text)
        specparser.set_android_p4a_whitelist(self.ids.android_p4a_whitelist.text)
        specparser.set_android_p4a_branch(self.ids.android_p4a_branch.text)
        specparser.set_android_entrypoint(self.ids.android_entrypoint.text)
        specparser.set_android_add_jars(self.ids.android_add_jars.text)
        specparser.set_android_add_src(self.ids.android_add_src.text)
        specparser.set_android_ouya_category(self.ids.android_ouya_category.text)
        specparser.set_android_ouya_icon(self.ids.android_ouya_icon_filename.text)
        specparser.set_android_manifest_intent_filters(self.ids.android_manifest_intent_filters.text)
        specparser.set_android_add_libs_armeabi(self.ids.android_add_libraries_armeabi.text)
        specparser.set_android_add_libs_armeabi_v7a(self.ids.android_add_libraries_armeabi_v7a.text)
        specparser.set_android_add_libs_x86(self.ids.android_add_libraries_x86.text)
        specparser.set_android_add_libs_mips(self.ids.android_add_libraries_mips.text)
        specparser.set_android_wakelock(self.ids.android_wakelock.text)
        specparser.set_android_meta_data(self.ids.android_meta_data.text)
        specparser.set_android_library_references(self.ids.android_library_references.text)

    def save_ios_settings(self):
        #TODO fix when iOS thoughts are done
        specparser.set_ios_codesign_debug(self.ids.ios_codesign_debug.text)
        specparser.set_ios_codesign_release()

    def save_other_settings(self):
        pass

    def save_buildozer_settings(self):
        specparser.set_buildozer_log_level(self.ids.buildozer_loglevel.text)
        specparser.set_buildozer_warn_on_root(self.ids.buildozer_warn_on_root.text)

    def revert_save(self, dt):
        self.ids.save_button.text = 'Save'


