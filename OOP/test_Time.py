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


@pytest.mark.parametrize(
    "time1, time2, expected_hours, expected_minutes, expected_seconds, should_raise_error",
    [
        (Time(1, 30, 45), Time(2, 15, 20), 3, 46, 5, False),
        (Time(23, 45, 59), Time(0, 30, 1), 0, 16, 0, False),
        (Time(10, 30, 45), Time(15, 45, 50), 26, 16, 45, True),
    ]
)
def test_add(time1, time2, expected_hours, expected_minutes, expected_seconds, should_raise_error):
    result = time1 + time2
    assert result.hours == expected_hours
    assert result.minutes == expected_minutes
    assert result.seconds == expected_seconds


@pytest.mark.parametrize("time1, time2, expected_hours, expected_minutes, expected_seconds", [
    (Time(10, 30, 45), Time(2, 15, 20), 8, 15, 25),
    (Time(5, 0, 0), Time(2, 30, 0), 2, 30, 0),
    (Time(1, 0, 0), Time(1, 0, 0), 0, 0, 0),
    (Time(0, 0, 0), Time(1, 0, 0), -1, 0,0),
])
def test_subtraction(time1, time2, expected_hours, expected_minutes, expected_seconds):
    result = time1 - time2
    assert result.hours == expected_hours
    assert result.minutes == expected_minutes
    assert result.seconds == expected_seconds

