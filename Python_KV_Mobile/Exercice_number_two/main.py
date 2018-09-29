import os
from kivy import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.bubble import Button
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
Config.set('graphics', 'multisamples', '0')


class Divisor(GridLayout):
    pass

class DivisorScreen(App):

    def build(self):
        return Divisor()


my_appp = DivisorScreen()
my_appp.run()