from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton, ListView
Builder.load_string("""
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import Window kivy.core.window.Window
#: import ListItemButton kivy.uix.listview.ListItemButton
<MyListView>:
    ListView:
        id:str
                    
        adapter:
            ListAdapter(
            cls=ListItemButton,
            data=["Item #{0}".format(i) for i in range(10)],
            args_converter=lambda row_index, rec:\
            'text': rec,'size_hint_y': None, 'height': 25})
            
""")


class MyListView(BoxLayout):
    pass

if __name__ == '__main__':
    runTouchApp(MyListView())
