import pytest
from kivy.clock import mainthread
from kivy.tests.common import UnitTestTouch
from kivy.tests.async_gui import AsyncUnitTouch
from main import ClockApp


def test_initial_time_label(app):
    assert app.label_time.text == app.current_time


def test_initial_date_label(app):
    assert app.label_date.text == app.current_date


def test_toggle_format_24_to_12(app):
    initial_time = app.label_time.text
    app.button_format.trigger_action()
    if ":" in initial_time:
        assert "AM" in app.label_time.text or "PM" in app.label_time.text
    else:
        assert ":" in app.label_time.text


def test_time_update(app):
    initial_time = app.label_time.text
    # Simulate time passing
    app.update_time(1)
    assert app.label_time.text != initial_time
    
def test_change_clock_color():
    clock_app = ClockApp()
    assert clock_app.label_time.color == (1, 1, 1, 1)
    clock_app.change_clock_color((1, 0, 0, 1))
    assert clock_app.label_time.color == (1, 0, 0, 1)
    
def test_current_day(clock_app):
    assert clock_app.current_day == datetime.now().strftime("%A")

def test_toggle_format(clock_app):
    initial_time = clock_app.current_time
    clock_app.toggle_format(None)
    assert clock_app.current_time != initial_time
    
def test_play_tick_sound(clock_app):
    # Since play_tick_sound method uses an external library (plyer), 
    # we can only test if the method executes without errors.
    clock_app.play_tick_sound()