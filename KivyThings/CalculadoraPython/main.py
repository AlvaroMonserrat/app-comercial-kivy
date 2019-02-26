


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
import __future__

#Definir tamano de Pantalla


#Config.set('graphics', 'resizable', 0)
#Window.size = (1080*0.5, 2240*0.5)


class CustomButton(Button):

    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)

        self.font_size = "30sp"



class Micalculadora(GridLayout):


    def press(self, button):

        try:
            int(button.text)
            self.ti.text += button.text


        except:
            signal = self.ti.text[-1:]
            if signal == "+" or signal == "-" or signal == "*" or signal == "/":
                self.ti.text += ""
            else:
                self.ti.text += button.text

    def deleteText(self, button):
        self.ti.text = ""


    def result(self, button):

        try:

            data_text = eval(compile(self.ti.text, '<string>', 'eval', __future__.division.compiler_flag))
            if isinstance(data_text, float):
                self.ti.text = str(data_text)[:10]
                self.ti.do_cursor_movement('cursor_home')

            else:
                self.ti.text = str(data_text)
                self.ti.do_cursor_movement('cursor_home')

        except:
            data_text = self.ti.text[:-1]
            self.ti.text = str(eval(data_text))
            self.ti.do_cursor_movement('cursor_home')




    def __init__(self, **kwargs):
        super(Micalculadora, self).__init__(**kwargs)

        self.rows = 5
        self.padding = "10dp"
        self.spacing = "10dp"

        bl = BoxLayout()
        self.add_widget(bl)
        self.ti = TextInput(font_size="40sp", multiline=False, readonly=True)
        bl.add_widget(self.ti)

        b2 = BoxLayout(spacing="7sp")
        self.add_widget(b2)
        b2.add_widget(CustomButton(text="7", on_press=self.press))
        b2.add_widget(CustomButton(text="8", on_press=self.press))
        b2.add_widget(CustomButton(text="9", on_press=self.press))
        b2.add_widget(CustomButton(text="+", on_press=self.press))

        b3 = BoxLayout(spacing="7sp")
        self.add_widget(b3)
        b3.add_widget(CustomButton(text="4", on_press=self.press))
        b3.add_widget(CustomButton(text="5", on_press=self.press))
        b3.add_widget(CustomButton(text="6", on_press=self.press))
        b3.add_widget(CustomButton(text="-", on_press=self.press))

        b4 = BoxLayout(spacing="7sp")
        self.add_widget(b4)
        b4.add_widget(CustomButton(text="1", on_press=self.press))
        b4.add_widget(CustomButton(text="2", on_press=self.press))
        b4.add_widget(CustomButton(text="3", on_press=self.press))
        b4.add_widget(CustomButton(text="*", on_press=self.press))

        b5 = BoxLayout(spacing="7sp")
        self.add_widget(b5)
        b5.add_widget(CustomButton(text="AC", on_press=self.deleteText))
        b5.add_widget(CustomButton(text="0", on_press=self.press))
        b5.add_widget(CustomButton(text="=", on_press=self.result))
        b5.add_widget(CustomButton(text="/", on_press=self.press))

class CalculadoraApp(App):

    def build(self):

        return Micalculadora()

CalculadoraApp().run()