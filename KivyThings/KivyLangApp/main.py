#App usando lenguaje Kivy

import kivy
kivy.require("1.10.1")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MainScreen(BoxLayout):

    def on_press_button(self):
        appKivy.root_window.remove_widget(appKivy.root)
        appKivy.root_window.add_widget(SecondScreen())



class SecondScreen(BoxLayout):

    def on_press_button(self):
        appKivy.root_window.remove_widget(appKivy.root)
        appKivy.root_window.add_widget(ThirdScreen())


class ThirdScreen(BoxLayout):

    def on_press_button(self):
        appKivy.root_window.remove_widget(appKivy.root)
        appKivy.root_window.add_widget(MainScreen())

    def on_press_button2(self):
        appKivy.root_window.remove_widget(appKivy.root)
        appKivy.root_window.add_widget(SecondScreen())


class KVapp(App):

    def build(self):
        return MainScreen()


appKivy = KVapp()

appKivy.run()