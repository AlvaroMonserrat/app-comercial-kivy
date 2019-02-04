#
from kivy.app import App
from kivy.uix.textinput import TextInput


def build():
    text_input = TextInput(text="Escriba Aqui")
    return text_input


appText = App()
appText.build = build
appText.run()