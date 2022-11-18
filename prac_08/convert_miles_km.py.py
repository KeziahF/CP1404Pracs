"""
CP1404 Practical
Kivy GUI program converting miles to km
"""

from kivy.app import App
from kivy.lang import Builder

FACTOR_MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """Main program - Kivy app converting miles to km"""

    def build(self):
        """Build the kivy GUI"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate(self, text):
        """calculate conversion and display on GUI"""
        miles = self.check_value(text)
        result = float(miles) * FACTOR_MILES_TO_KM
        self.root.ids.output_km.text = str(result)

    def increment(self, text, change):
        """Increase or decrease the miles value by 1"""
        result = self.check_value(text) + change
        self.root.ids.input_miles.text = str(result)

    def check_value(self, text):
        """Confirm entered value is valid for calculations"""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
