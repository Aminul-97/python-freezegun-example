import pytest
from freezegun import freeze_time
from datetime import datetime

def get_greeting():
    current_time = datetime.now()
    if current_time.hour < 12:
        return "Good morning!"
    elif 12 <= current_time.hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"


# Test case without freezing time
def test_get_greeting_default():
    # This test will depend on the actual time when the test is run
    greeting = get_greeting()
    assert greeting in ["Good morning!", "Good afternoon!", "Good evening!"]

# Test case with frozen time using freezegun
@freeze_time("2023-01-01 12:00:00")
def test_get_greeting_frozen_time():
    # This test will always use the frozen time, so the result is predictable
    greeting = get_greeting()
    assert greeting == "Good afternoon!"

# Another test case with a different frozen time
@freeze_time("2023-01-01 20:00:00")
def test_get_greeting_frozen_time_evening():
    greeting = get_greeting()
    assert greeting == "Good evening!"

