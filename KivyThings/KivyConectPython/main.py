

import kivy
kivy.require("1.10.1")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MiCaja(BoxLayout):

    def click(self):
        print("SI")
        self.ids.lb1.text = "Programminng"
        self.ids.lb2.text = "Connecting"

class FirstApp(App):

    def funcApp(self):
        print("Click app func")


ventana = FirstApp()
ventana.run()