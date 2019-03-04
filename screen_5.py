from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.app import App
from kivy.properties import StringProperty
from kivymd.navigationdrawer import NavigationDrawer
from kivy.core.window import Window
from kivy.animation import Animation
class Screen5(Screen):
    imagesource=StringProperty('kt6.png ')
    def chg(self):
        self.imagesource='anu.jpg'
    def antry(self):
        anim = Animation(x=(160))+Animation(x=(165))
        
        anim.repeat=True
        self.a = App.get_running_app()
        anim.start(self.a.root.ids.annav.ids.nav1)
        anim = Animation(y=(50))+Animation(y=(60))
        anim.repeat=True
        self.a = App.get_running_app()
        anim.start(self.a.root.ids.annav.ids.nav2)
        self.a.root.current='screen_6'
        
        
        
        
