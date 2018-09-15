"""

"""

from kivy.app import App
from kivy.lang import Builder

__author__ = 'Ryan Honorica'

METERS_TO_KM = 0.001


class MetersConverterApp(App):
    """ MetersConverterApp is a Kivy App for converting meters to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Meters to Kilometres"
        self.root = Builder.load_file('convert_m_to_km_custom')
        return self.root

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        value = self.get_validated_meters()
        result = value * METERS_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """
        handle up/down button press, update the text input with new value, call calculation function
        :param change: the amount to change
        """
        value = self.get_validated_meters() + change
        self.root.ids.input_meters.text = str(value)
        self.handle_calculate()

    def get_validated_meters(self):
        """
        get text input from text entry widget, convert to float
        :return: 0 if error, float version of text if valid
        """
        try:
            value = float(self.root.ids.input_meters.text)
            return value
        except ValueError:
            return 0


MetersConverterApp().run()
