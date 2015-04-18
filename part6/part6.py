
import random

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ListProperty


class ScatterTextWidget(BoxLayout):

    text_color = ListProperty([1, 0, 0, 1])

    def change_label_color(self, *args):
        color = [random.random() for i in range(3)] + [1]
        self.text_color = color


class TutorialApp(App):

    def build(self):
        return ScatterTextWidget()


if __name__ == "__main__":
    TutorialApp().run()