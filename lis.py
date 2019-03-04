from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton, ListView

data = [{'text': str(i), 'is_selected': False} for i in range(100)]

args_converter = lambda row_index, rec: {'text': rec['text'],
                                             'size_hint_y': None,
                                             'height': 25,
                                             'color':[0,0,0,1]}

list_adapter = ListAdapter(data=data,
                               args_converter=args_converter,
                               cls=ListItemButton,
                               selection_mode='single',
                               allow_empty_selection=False)

list_view = ListView(adapter=list_adapter)
