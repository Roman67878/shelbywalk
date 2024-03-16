from Time import Time, TimeStamp, TimeValueError
from freezegun import freeze_time
from unittest import mock
import pytest


@pytest.mark.parametrize(
    ('hours', 'minutes', 'seconds'),
    [
        (12, 23, 12),
        (23, 23, 12),
        (3, 19, 2)
    ]
)
def test_init(hours, minutes, seconds):
    time1 = Time(hours, minutes, seconds)
    assert time1.hours == hours
    assert time1.minutes == minutes
    assert time1.seconds == seconds


@pytest.mark.parametrize(
    ('input_time', 'hours', 'minutes', 'seconds'),
    [
        ('12:23:34', 12, 23, 34)
    ]
)
def test_input_time(input_time, hours, minutes, seconds):
    time2 = Time()
    with mock.patch('builtins.input', return_value="12:23:34"):
        time2.input_time()
    assert time2.hours == hours
    assert time2.minutes == minutes
    assert time2.seconds == seconds


@pytest.mark.parametrize(
    ('hours', 'minutes', 'seconds', 'result'),
    [
        (12, 23, 34, "Время: 12:23:34"),
        (8, 20, 34, "Время: 8:20:34"),
        (12, 20, 10, "Время: 12:20:10"),
        # (ы, ы, ы, "ы:ы:ы")
        (13, 15, 12, "Время: 13:15:12")
    ]
)
def test_str(hours, minutes, seconds, result):
    time3 = Time(hours, minutes, seconds)
    assert str(time3) == result


@freeze_time("23:30:30")
def test_init():
    time4 = TimeStamp()
    assert time4.hours == 23
    assert time4.minutes == 30
    assert time4.seconds == 30


@pytest.mark.parametrize("time1, time2, result", [
    (Time(5, 30, 45), Time(2, 15, 10), Time(7, 45, 55)),
    (Time(12, 35, 20), Time(2, 10, 20), Time(15, 0, 40)),
    (Time(23, 58, 58), Time(4, 4, 4), Time(4, 2, 2))
])
def test_sub(time1, time2, result):
    result = time1 + time2
    assert result == result


@pytest.mark.parametrize("hours1, minutes1, seconds1,"
                         "hours2, minutes2, seconds2,"
                         " expected_hours, expected_minutes, expected_seconds",
[
  (10, 30, 45, 2, 15, 20, 8, 15, 25),
  (5, 0, 0, 2, 30, 0, 2, 30, 0),
  (1, 0, 0, 1, 0, 0, 0, 0, 0),
  (24, 0, 0, 1, 0, 0, 23, 0, 0),
]
)
def test_subtraction(hours1, minutes1, seconds1, hours2, minutes2, seconds2, expected_hours, expected_minutes,
                     expected_seconds):
    result = Time(hours1, minutes1, seconds1) - Time(hours2, minutes2, seconds2)
    assert Time(hours1, minutes1, seconds1) - Time(hours2, minutes2, seconds2) == result
