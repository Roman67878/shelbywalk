from Time import Time
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


def test_input(mocker):
    mocker.patch('monkey.input', input_time="12:23:34")
    time2 = Time()
    assert time2.hours == 12
    assert time2.minutes == 23
    assert time2.seconds == 34


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
    assert Time.__str__(Time(hours, minutes, seconds)) == result
