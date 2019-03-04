from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.app import App

class Screen3(Screen):
    def terms(self):
        self.a = App.get_running_app()
        self.a.root.current='screen_4'
    def agree(self):
        self.a = App.get_running_app()
        self.a.root.current='screen_5'
