from kivy.app import App
from kivy.uix.widget import Widget


class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()



btn1 = Button(text='Hello world 1')
btn1.bind(on_press=callback)

PongApp().run()
