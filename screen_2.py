from kivy.uix.screenmanager import ScreenManager ,Screen
from kivy.app import App
from kivy.animation import Animation
class Screen2(Screen):
    def verify(self,txt2text):
        tr=txt2text
        print(tr)
        self.a = App.get_running_app()
        td=self.a.nu
        if(str(tr)==str(td)):
            anim = Animation(y=(410))+Animation(y=(420))
            anim.repeat=True
            self.a = App.get_running_app()
            anim.start(self.a.root.ids.scr3.ids.log)
            self.a.root.current='screen_3'
           
        
