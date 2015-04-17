from kivy.app import App

from kivy.uix.boxlayout import BoxLayout


class ScatterTextWidget(BoxLayout):

    pass


class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == "__main__":
    TutorialApp().run()