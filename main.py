import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

## will hold the design elements of the app
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid,self).__init__(**kwargs)



## executing the app
class MyApp(App):

    def build(self):
        return Label(text = "Hello!")

if __name__ == '__main__':
    MyApp().run()