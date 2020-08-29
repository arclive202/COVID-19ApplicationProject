#FROM KIVYAPPFILE4 WE WILL WORK WITH BUILDING OUT THE CHAT PAGE

#You will be importing the client socket py file here and make use of its function to establish connection.

import kivy
from kivy.app import App    # base app class
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
import os
import sys
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import socket_client

#rather than making a linear flow of screens, we make use of the screen manager to manage between the flow of screens

kivy.require("1.11.1")


class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)     #you are basically referring to the Grid Layout
        self.cols = 2  # so imagine you got two columns but infinite rows

        if os.path.isfile("prev_details.txt"):
            with open("prev_details.txt", "r") as f:
                d = f.read().split(",")
                prev_ip = d[0]
                prev_port = d[1]
                prev_username = d[2]
        else:
            prev_ip = ''
            prev_port = ''
            prev_username = ''

        self.add_widget(Label(text="IP:"))
        self.ip = TextInput(text=prev_ip, multiline=False)
        self.add_widget(self.ip)

        self.add_widget(Label(text="Port:"))
        self.port = TextInput(text=prev_port, multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text="Username:"))
        self.username = TextInput(text=prev_username, multiline=False)
        self.add_widget(self.username)

        self.join = Button(text="Join")         # just these two lines are going to give you a button at the bottom left
        self.join.bind(on_press=self.join_button)   # now we're going to go ahead and create a button function
        self.add_widget(Label())
        self.add_widget(self.join)             # now that you have the button. The task is to go ahead and bind it to something

    def join_button(self, instance):
        port = self.port.text
        ip = self.ip.text
        username = self.username.text

        #print(f"Attempting to join {ip}:{port} as {username}")
        with open("prev_details.txt", "w") as f:
            f.write(f"{ip},{port},{username}")

        info = f"Attempting to join {ip}:{port} as {username}"
        chat_app.info_page.update_info(info)
        chat_app.screen_manager.current = "Info"
        Clock.schedule_once(self.connect, 1)

    def connect(self, _):
        port = int(self.port.text)
        ip = self.ip.text
        username = self.username.text

        if not socket_client.connect(ip,port,username,show_error):  #incase we are not able to connect to server
            return

        chat_app.create_chat_page()
        chat_app.screen_manager.current = "Chat"



class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign="center", valign="middle", font_size=30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)

    def update_info(self, message):
        self.message.text = message

    def update_text_width(self, *_):
        self.message.text_size = (self.message.width * 0.9, None)

class ChatPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="Hey! Atleast it connected!"))



class DemoApp(App):
    def build(self):                # pretty much an initialisation method / Rather than connect page as in the previous file, we are now going to call the screen manager here
        self.screen_manager = ScreenManager()

        self.connect_page = ConnectPage()           #These 4 lines are for one page
        screen = Screen(name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.info_page = InfoPage()                 #similarly you can make N number of pages
        screen = Screen(name="Info")
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

    def create_chat_page(self):
        self.chat_page = ChatPage()
        screen = Screen(name="Chat")
        screen.add_widget(self.chat_page)
        self.screen_manager.add_widget(screen)

def show_error(message):
    chat_app.info_page.update_info(message)
    chat_app.screen_manager.current = "Info"
    Clock.schedule_once(sys.exit, 10)



if __name__ == "__main__":
    chat_app = DemoApp()
    chat_app.run()                 # main intention would be to return the Connect Page


