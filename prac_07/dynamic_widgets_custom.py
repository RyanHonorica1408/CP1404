"""
CP1404 Prac 7 Dynamic Widget code, by Ryan Honorica.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetsApp_custom(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    name = {"Bob Brown", "Cat Cyan", "Oren Ochre"}

    def build(self):

        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets_custom')
        self.create_widgets()
        return self.root

    def create_widgets(self):

        for name in self.names:
            label = Label(text=name)
            self.root.ids.entries_box.add_widget(label)


DynamicWidgetsApp_custom().run()

