import kivy
kivy.require('2.1.0') # replace with your current kivy version !
from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '400')
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial

class GUI(App):
    screen=None
    timeline=None
    mylist=None
    list_valid=None
    def __init__(self,**kwargs):
        super(GUI,self).__init__(**kwargs)
        self.screen=BoxLayout(orientation='vertical')
        self.mylist=[]
        self.command_list = []
        self.list_valid=False
        self.timeline=BoxLayout(orientation='horizontal')
        # initialize buttons
        self.submit = Button(text="submit")
        self.clear = Button(text="clear")

        self.btn_1 = Button(text="go forward")
        self.btn_2 = Button(text="go back")
        self.btn_3 = Button(text="go left")
        self.btn_4 = Button(text="go right")
        self.btn_5 = Button(text="look left")
        self.btn_6 = Button(text="look right")
        self.btn_7 = Button(text="turn left")
        self.btn_8 = Button(text="stop")

        self.screen.add_widget(self.submit)
        self.submit.bind(on_press=partial(self.submitFunc))

        self.screen.add_widget(self.clear)
        self.clear.bind(on_press=partial(self.del_command_list))

        # function buttons move to timeline and are added to command list on click
        self.screen.add_widget(self.btn_1)
        self.btn_1.bind(on_press=partial(self.update_label))
        self.btn_1.bind(on_press=partial(self.set_command_list))

        self.screen.add_widget(self.btn_2)
        self.btn_2.bind(on_press=partial(self.update_label))
        self.btn_2.bind(on_press=partial(self.set_command_list))
        self.screen.add_widget(self.btn_3)
        self.btn_3.bind(on_press=partial(self.update_label))
        self.btn_3.bind(on_press=partial(self.set_command_list))
        self.screen.add_widget(self.btn_4)
        self.btn_4.bind(on_press=partial(self.update_label))
        self.btn_4.bind(on_press=partial(self.set_command_list))
        self.screen.add_widget(self.btn_5)
        self.btn_5.bind(on_press=partial(self.update_label))
        self.btn_5.bind(on_press=partial(self.set_command_list))
        self.screen.add_widget(self.btn_6)
        self.btn_6.bind(on_press=partial(self.update_label))
        self.btn_6.bind(on_press=partial(self.set_command_list))
        self.screen.add_widget(self.btn_7)
        self.btn_7.bind(on_press=partial(self.update_label))
        self.btn_7.bind(on_press=partial(self.set_command_list))
        self.screen.add_widget(self.btn_8)
        self.btn_8.bind(on_press=partial(self.update_label))
        self.btn_8.bind(on_press=partial(self.set_command_list))

        self.screen.add_widget(self.timeline)
        for i in range(8):
            self.mylist.append(Label(text="empty"))
            self.timeline.add_widget(self.mylist[i])

    def update_label(self, win):
        for i in range(8):
            if self.mylist[i].text is "empty":
                self.mylist[i].text = win.text
                break

    def set_command_list(self, win):
        self.command_list.append(win.text)
        print(self.command_list)

    # clear button calls this, deletes commands and empties timeline
    def del_command_list(self, win):
        self.command_list = []
        for i in range(8):
            self.mylist[i].text = "empty"
        print(self.command_list)
    
    def submitFunc(self, win):
        self.list_valid=True

    def get_response(self):
        if self.list_valid:
            self.list_valid=False
            return self.command_list
        return None

    def build(self):
        return self.screen


#GUI().run()
