from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from datetime import datetime


class ClockApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self._current_time = datetime.now().strftime("%H:%M:%S")
        self._current_date = datetime.now().strftime("%Y-%m-%d")
        self._is_24hr_format = True

        self.label_time = Label(text=self._current_time, font_size=80)
        self.label_date = Label(text=self._current_date, font_size=30)

        self.button_format = Button(text="Toggle Format", size_hint=(1, 0.1))
        self.button_format.bind(on_press=self.toggle_format)

        self.add_widget(self.label_time)
        self.add_widget(self.label_date)
        self.add_widget(self.button_format)

        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, dt):
        self.current_time = datetime.now().strftime("%H:%M:%S")
        self.current_date = datetime.now().strftime("%Y-%m-%d")

    def toggle_format(self, instance):
        self._is_24hr_format = not self._is_24hr_format
        if self._is_24hr_format:
            self.label_time.text = datetime.now().strftime("%H:%M:%S")
        else:
            self.label_time.text = datetime.now().strftime("%I:%M:%S %p")

    @property
    def current_time(self):
        return self._current_time

    @current_time.setter
    def current_time(self, value):
        self._current_time = value
        self.label_time.text = value

    @property
    def current_date(self):
        return self._current_date

    @current_date.setter
    def current_date(self, value):
        self._current_date = value
        self.label_date.text = value


class ClockAppMain(App):
    def build(self):
        return ClockApp()


if __name__ == "__main__":
    ClockAppMain().run()