import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager
from random import randint
import random

class MyApp(App):
    theme_cls=ThemeManager()
    nu = random.randint(1111,9999)
    print(nu)
    def build(self):
        self.load_kv('kt.kv')

MyApp().run()
