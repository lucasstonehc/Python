# coding: utf-8

import os
from kivy import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.bubble import Button
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
Config.set('graphics', 'multisamples', '0')


class Menu(BoxLayout):

    def on_press_btn(self):
        my_app.root_window.remove_widget(my_app.root)
        my_app.root_window.add_widget(Menu2())



class Menu2(BoxLayout):

    def on_press_btn(self):
        my_app.root_window.remove_widget(my_app.root)
        my_app.root_window.add_widget(Menu())


class MyApp(App):

    def build(self):
        return Menu2()


my_app = MyApp()
my_app.run()