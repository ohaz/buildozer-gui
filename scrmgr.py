from kivy.uix.screenmanager import ScreenManager, SlideTransition

sm = None
screens = None
last_screen = None

def init():
    global sm
    sm = ScreenManager(transition=SlideTransition())

def set_screens(set_screens):
    global screens
    screens = set_screens

def get_screens():
    return screens

def get_sm():
    return sm

def switch_to(screen):
    global last_screen
    last_screen = sm.current_screen
    sm.switch_to(screen)

def get_screen(name):
    for s in screens:
        if (s.name == name):
            return s