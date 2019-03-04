from kivy.uix.screenmanager import ScreenManager,Screen
import kivy
from os import getcwd
from os.path import exists
from os.path import splitext
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.graphics import Line
from kivy.graphics import *
from kivy.uix.image import Image  
from kivy.uix.behaviors import ButtonBehavior 
from kivy.properties import ObjectProperty,StringProperty,NumericProperty,ReferenceListProperty
from kivymd.navigationdrawer import NavigationDrawer
from kivymd.button import MDIconButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.logger import Logger
from plyer import camera
from kivy.app import platform


class Screen6(Screen):
    #nav2=ObjectProperty(None)
    def __init__(self, **kwargs):
        super(Screen6, self).__init__(**kwargs)
        self.cwd = getcwd() + "/"
        
    def chgscr(self):
        self.ids.btn1.my_color=(0,0,0)
        self.ids.btn.my_color=(0,128,0)
        self.ids.btn2.my_color=(0,0,0)
        self.a = App.get_running_app()
        self.sm.current='screen_one'
        
    def chgscr1(self):
        self.ids.btn1.my_color=(0,128,0)
        self.ids.btn.my_color=(0,0,0)
        self.ids.btn2.my_color=(0,0,0)
        self.a = App.get_running_app()
        self.sm.current='screen_two'
    def chgscr2(self):
        self.ids.btn1.my_color=(0,0,0)
        self.ids.btn.my_color=(0,0,0)
        self.ids.btn2.my_color=(0,128,0)
        self.a = App.get_running_app()
        self.sm.current='screen_three'
    def do_capture(self):
        data_dir =  App().user_data_dir
        res='data_dir'+ 'DCIM'
        filepath = res + self.ids.filename_text.text
       
        print(filepath)
        ext = splitext(filepath)[-1].lower()

        if(exists(filepath)):
            popup = Popup(title='error',content=Label(text="Picture with this name already exists!"),size_hint=(0.6,0.3))
            popup.open()
            return False

        try:
            camera.take_picture(filename=filepath,
                                on_complete=self.camera_callback)
        except NotImplementedError:
            popup = Popup(title='error',content=Label(text="This feature has not yet been implemented for this platform."),size_hint=(0.6,0.3))
            popup.open()

    def camera_callback(self, filepath):
        if(exists(filepath)):
            popup = Popup(title='error',content=Label(text="Picture saved!"),size_hint=(0.6,0.3))
            popup.open()
        else:
            popup = Popup(title='error',content=Label(text="Could not save your picture!"),size_hint=(0.6,0.3))
            popup.open()
    def on_pause(self):
        return True

    def on_resume(self):
        pass    
    def closeit(self):
        self.ids.bx.remove_widget(self.ids.bx1)        

        
        
        #self.ids.btn1.canvas.after.add(Rectangle(size=(100,100)))
            
class ImageButton(ButtonBehavior,Image):
    def on_press(self):
        self.a = App.get_running_app()
        self.a.root.current='screen_7'
        print('pressed')
