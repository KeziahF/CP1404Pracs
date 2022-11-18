"""
CP1404 Practical
Kivy GUI program to demonstrate dynamic labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DyanmicLabels(App):
    """Main program - Kivy app demonstrating dynamic labels"""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.names = ['Bob', 'Sarah', 'Tina', 'George']

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create a label for each name in the list and display in GUI"""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)


DyanmicLabels().run()
