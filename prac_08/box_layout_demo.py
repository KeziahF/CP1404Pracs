"""
CP1404 Practical
Kivy GUI program demonstrating box layout
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Main program - Kivy app demonstrating box layout"""

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Output Hello + user name to label on GUI"""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear(self):
        """Clear user entry and display from GUI"""
        self.root.ids.output_label.text = ''
        self.root.ids.input_name.text = ''


BoxLayoutDemo().run()
