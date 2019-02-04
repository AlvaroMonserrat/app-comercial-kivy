from kivy.app import App
from kivy.uix.label import Label




#Se crea una clase hija de App
class MiProgram(App):

    def build(self):
        return Label()


MiProgram().run()
