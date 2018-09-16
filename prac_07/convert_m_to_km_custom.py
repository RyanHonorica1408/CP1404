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
        value = self.get_validated_meters()
        result = value * METERS_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """
        """
        value = self.get_validated_meters() + change
        self.root.ids.input_meters.text = str(value)
        self.handle_calculate()

    def get_validated_meters(self):
        """
        """
        try:
            value = float(self.root.ids.input_meters.text)
            return value
        except ValueError:
            return 0


MetersConverterApp().run()
