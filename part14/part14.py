
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import time
import random


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class ColorScreen(Screen):
    color = ListProperty([1, 0, 0, 1])


class MyScreenManager(ScreenManager):

    def new_color_screen(self):
        name = str(time.time())
        s = ColorScreen(name=name,
                        color=[random.random() for i in range (3)] + [1])
        self.add_widget(s)
        self.current = name


root_widget = Builder.load_string('''

#:import random random.random
#:import FadeTransition kivy.uix.screenmanager.FadeTransition

MyScreenManager:
    transition: FadeTransition()
    FirstScreen:
    SecondScreen:

<FirstScreen>:
    name: "first"
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "first screen!"
            font_size: 30
        Image:
            source: "colours.png"
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            Button:
                text: "goto second screen"
                font_size: 30
                on_press: app.root.current = "second"
            Button:
                text: "get random color screen"
                font_size: 30
                on_press: app.root.new_color_screen()

<SecondScreen>:
    name: "second"
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "second screen!"
            font_size: 30
        Image:
            source: "colours2.png"
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            Button:
                text: "goto first screen"
                font_size: 30
                on_press: app.root.current = "first"
            Button:
                text: "get random color screen"
                font_size: 30
                on_press: app.root.new_color_screen()

<ColorScreen>:
    BoxLayout:
        orientation: "vertical"
        color: random(), random(), random(), 1
        Label:
            text: "color {:.2},{:.2},{:.2} screen".format(*root.color[:3])
            font_size: 30
        Widget:
            canvas:
                Color:
                    rgba: root.color
                Ellipse:
                    pos: self.pos
                    size: self.size
        BoxLayout:
            Button:
                text: "goto first screen"
                font_size: 30
                on_press: app.root.current = "first"
            Button:
                text: "get random color screen"
                font_size: 30
                on_press: app.root.new_color_screen()

''')


class ScreenManagerApp(App):

    def build(self):
        return root_widget


ScreenManagerApp().run()