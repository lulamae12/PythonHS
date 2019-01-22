from kivy.app import App
from kivy.uix.gridlayout import GridLayout
Builder.load_string("kivyTest.kv")
class Container(GridLayout):
    pass
class KivyTestApp(App):
    def build(self):
        self.title = "tars"
        return Container()
app = MainApp
app.run(self)
