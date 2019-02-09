#App utilizando solo lenguaje Python

import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class TelaUno(BoxLayout):

    def on_press_bt(self):
        window.root_window.remove_widget(window.root)
        window.root_window.add_widget(TelaDos())

    #super clase: permite traer la funcion init de la clase BoxLayout
    def __init__(self, **kwargs):
        super(TelaUno, self).__init__(**kwargs)
        self.orientation = "vertical"
        button_1 = Button(text="Clic")
        button_1.background_color = 0.3, 0.5, 0.2, 1
        button_1.on_press = self.on_press_bt #Linkea la funcion on_press con la funcion generada
        self.add_widget(button_1)
        self.add_widget(Button(text="Botton 2"))
        self.add_widget(Button(text="Botton 3"))

class TelaDos(BoxLayout):

    def on_press_bt(self):
        window.root_window.remove_widget(window.root)
        window.root_window.add_widget(TelaUno())

    def __init__(self, **kwargs):
            super(TelaDos, self).__init__(**kwargs)
            self.orientation = "vertical"

            button_2 = Button(text="Clic")
            button_2.on_press = self.on_press_bt

            self.add_widget(button_2)

class KVvsPy(App):


    def build(self):
        return TelaUno()


window = KVvsPy()

window.run()



