"""
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicWidgetsApp_custom(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """
        Construct main app.
        """
        super().__init__(**kwargs)
        self.name= {"Bob Brown", "Cat Cyan", "Oren Ochre"}

    def build(self):
        """
        Build the Kivy GUI.
        :return: reference to the root Kivy widget
        """
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets_custom')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """
        Create buttons and add them to the GUI
        :return: None
        """
        for name in self.name:
            # create a button for each phonebook entry, specifying the text and id
            # (although text and id are the same in this case, you should see how this works)
            temp_button = Button(text=name, id=name)
            temp_button.bind(on_release=self.press_entry)
            # add the button to the "entries_box" using add_widget()
            self.root.ids.entries_box.add_widget(temp_button)

DynamicWidgetsApp_custom().run()
