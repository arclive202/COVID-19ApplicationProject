import kivy
from kivy.app import App    # base app class
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
import os
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

        print(f"Attempting to join {ip}:{port} as {username}")
        with open("prev_details.txt", "w") as f:
            f.write(f"{ip},{port},{username}")


class DemoApp(App):
    def build(self):                # pretty much an initialisation method
        return ConnectPage()

if __name__ == "__main__":
    DemoApp().run()                 # main intention would be to return the Connect Page


