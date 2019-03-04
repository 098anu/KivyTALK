from __future__ import print_function
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.animation import Animation
import sqlite3
from kivy.uix.recycleview import RecycleView
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from kivy.uix.image import Image
from kivy.uix.listview import ListItemButton
from kivy.uix.listview import ListView
from kivy.uix.behaviors import ButtonBehavior 
from kivy.properties import ObjectProperty,StringProperty,NumericProperty,ReferenceListProperty
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivymd.navigationdrawer import NavigationDrawer
from kivymd.button import MDIconButton
from kivy.uix.screenmanager  import ScreenManager,Screen

SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']

class Screen7(Screen):
    def __init__(self,**kwargs):
        super(Screen7,self).__init__(**kwargs)
    def animate(self):
        anim = Animation(x=(160))+Animation(x=(165))
        anim.repeat=True
        anim.start(self.ids.nav1)
    def chg(self):
        self.a = App.get_running_app()
        self.a.root.current='screen_6'
class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        creds = None
        n=10
        da=[]
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('people', 'v1', credentials=creds)

        # Call the People API
        print('List all connection names')
        results = service.people().connections().list(
            resourceName='people/me',
            pageSize=100,
            personFields='names,emailAddresses,phoneNumbers').execute()
        connections = results.get('connections', [])

        for person in connections:
            names = person.get('names', [])
            emailid=person.get('emailAddresses', [])
            phoneno=person.get('phoneNumbers', [])
            
            if phoneno:
                phone = phoneno[0].get('value')
                a=len(phone)
                if(a>=10):
                    if names:
                        name = names[0].get('displayName')
                        print(name)
                        
                        da.append(name)
                        
                        
                    
                    if emailid:
                        emai = emailid[0].get('value')
                        print(emai)
                    print(phone)
                    print('\n')
                    self.data=[{'text': str(x),'icon':'face'} for x in da]
                    self.data = sorted(self.data, key=lambda x: x['text'])
class ImageButton(ButtonBehavior,Image):
    def on_press(self):
        print('pressed')

