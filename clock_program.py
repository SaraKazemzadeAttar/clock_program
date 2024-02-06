from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from datetime import datetime
from plyer import notification
import calendar


class ClockApp(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = "vertical"
        self._current_time = datetime.now().strftime("%H:%M:%S")
        self._current_date = datetime.now().strftime("%Y-%m-%d")
        self._current_day = calendar.day_name[datetime.now().weekday()]
        self._is_24hr_format = True

        self.label_time = Label(text=self._current_time, font_size=80)
        self.label_date = Label(text=self._current_date, font_size=30)
        self.label_day = Label(text=self._current_day, font_size=30)

        self.button_format = Button(text="Toggle Format", size_hint=(1, 0.1))
        self.button_format.bind(on_press=self.toggle_format)

        self.add_widget(self.label_time)
        self.add_widget(self.label_date)
        self.add_widget(self.label_day)
        self.add_widget(self.button_format)

        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, dt):
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        self.current_date = now.strftime("%Y-%m-%d")
        self.current_day = calendar.day_name[now.weekday()]

    def toggle_format(self, instance):
        self._is_24hr_format = not self._is_24hr_format
        if self._is_24hr_format:
            self.label_time.text = datetime.now().strftime("%H:%M:%S")  # Update label with 24-hour format
        else:
            self.label_time.text = datetime.now().strftime("%I:%M:%S %p")  # Update label with 12-hour format

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

    @property
    def current_day(self):
        return self._current_day

    @current_day.setter
    def current_day(self, value):
        self._current_day = value
        self.label_day.text = value

    def play_tick_sound(self):
        # Use plyer to play a notification sound
        notification.notify(title='Clock Tick', message='', timeout=1)

    def change_clock_color(self, color):
        self.label_time.color = color


class ClockAppMain(App):
    def build(self):
        clock_app = ClockApp()
        clock_app.change_clock_color((1, 0, 0, 1))  # Set the clock color to red (RGB: 1, 0, 0)
        return clock_app


def main():
    ClockAppMain().run()


if __name__ == "__main__":
    main()