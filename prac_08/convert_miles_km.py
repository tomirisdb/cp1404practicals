"""
Estimated time: 45 minutes
Actual time: 40 minutes
Pseudocode:
MILES_TO_KM = 1.60934
class MilesConverterApp(App)
    function build(self)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    function handle_calculate(self)
        value = self.get_valid_input()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    function handle_increment(self, change)
        value = self.get_valid_input() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    function get_valid_input(self)
        try
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError
            return 0
"""
from kivy.app import App, Builder


MILES_TO_KM = 1.60934  # Conversion factor for miles to kilometers.


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handles the calculation of converting miles to kilometers."""
        value = self.get_valid_input()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Handles the increment of input miles."""
        value = self.get_valid_input() + change  # Increment or decrement the input miles value.
        self.root.ids.input_miles.text = str(value)  # Update the input miles field
        self.handle_calculate()

    def get_valid_input(self):
        """Gets a valid numerical input from the input field."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
