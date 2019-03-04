from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.dialog import MDDialog
from kivy.app import App
import random
from twilio.rest import Client
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

class Screen1(Screen):
    def verify(self,txt1text):
        tr=txt1text
        print(tr)
        global nu
        if(len(tr)<12):
            
            self.dialog = MDDialog(title="ERROR",
                                   content=Label(
                                   text= "Phone Number is incorrect",
                                   
                                   color=(0,0,0,1)),
                                   size_hint=(0.8,None),
                                   height=150,
                                   )
            self.dialog.add_action_button("OK",action=lambda *x:self.dismiss())
            self.dialog.open()
        else:
            self.a = App.get_running_app()
            self.a.root.current='screen_2'
            
            client = Client("ACd832558ee7761e48707545b31fc129c6", "81ab6aba1e8cc75d9d42c9a98cd4060b")


            client.messages.create(to="+919661197143", 
                       from_="+12252303008", 
                       body="please enter this otp"+str(self.a.nu)+"to login")

    def dismiss(self):
        self.dialog.dismiss()
      
            
            
