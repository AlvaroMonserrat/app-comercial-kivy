#Resolucion PC: 1920x1080 px
#Widget: Todos los elementos (componentes) visuales y que gestionan eventos


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


#Se crea una clase hija de FloatLayout
class RootWidget(FloatLayout):
    pass


#Se crea una clase hija de App
class MedidaApp(App):

    def build(self):
        return RootWidget()


MedidaApp().run()
