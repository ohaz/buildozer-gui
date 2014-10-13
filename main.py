# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App

import scrmgr
from mainmenu import Mainmenu, CreateProject, LoadProject

scrmgr.init()
scrmgr.set_screens([Mainmenu(name='mainmenu'), CreateProject(name='createproject'), LoadProject(name='loadproject')])
scrmgr.get_sm().switch_to((scrmgr.get_screens())[0])

class BuildozerGUIApp(App):
    def build(self):
        return scrmgr.get_sm()

if __name__ == '__main__':
    BuildozerGUIApp().run()