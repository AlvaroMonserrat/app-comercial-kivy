


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.core.window import Window

#Definir tamano de Pantalla
Config.set('graphics', 'resizable', 0)
Window.size = (1080*0.5, 2240*0.4)


class CalculadoraApp(App):
    pass

CalculadoraApp().run()