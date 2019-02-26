

import kivy
kivy.require("1.10.1")
from kivy.app import App



code = """


BoxLayout:
    Button:
        text: "1"
    Button:
        text: "2"



"""

from kivy.lang import Builder


class FirstApp(App):
    def build(self):
            return Builder.load_string(code)

ventana = FirstApp()
ventana.run()