from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.lang import Builder
from kivy.base import runTouchApp


Builder.load_string('''

<RootWidget>:
    text: "THE BACKGROUND"
    font_size: 100
    Image:
        source: "colours.png"
        allow_stretch: True
        keep_ratio: False
    Image:
        source: "colours2.png"
        allow_stretch: True
        keep_ratio: False
    Image:
        source: "colours.png"
        allow_stretch: True
        keep_ratio: False
''')


class RootWidget(Label):

    def do_layout(self, *args):
        num_children = len(self.children)
        width = self.width
        width_per_child = width / num_children

        positions = range(0, width, int(width_per_child))
        for position, child in zip(positions, self.children):
            child.height = self.height
            child.x = self.x + position
            child.y = self.y
            child.width = width_per_child

    def on_size(self, *args):
        self.do_layout()

    def on_position(self, *args):
        self.do_layout()

    def add_widget(self, widget):
        super(RootWidget, self).add_widget(widget)
        self.do_layout()

    def remove_widget(self, widget):
        super(RootWidget, self).remove_widget(widget)
        self.do_layout()


runTouchApp(RootWidget())