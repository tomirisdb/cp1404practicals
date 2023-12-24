"""
Estimated time: 20 minutes
Actual time: 20 minutes
class DynamicLabelsApp(App)
    function build(self)
        names = list
        main_layout = BoxLayout(orientation='vertical')
        for name in names
            label = Label(text=name, font_size=20)
            main_layout.add_widget(label)

        return main_layout
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy App that dynamically creates Labels for a list of names."""
    def build(self):
        """Build the main application layout"""
        names = ["Tomiris", "Dana", "Zhasmin", "Diyora", "Anelya", "Ikram"]

        # Creating the main layout
        main_layout = BoxLayout(orientation='vertical')

        # Dynamically create Labels for each name using for loop
        for name in names:
            label = Label(text=name, font_size=20)
            main_layout.add_widget(label)

        return main_layout


if __name__ == '__main__':
    DynamicLabelsApp().run()

