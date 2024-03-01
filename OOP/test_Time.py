from Time import Time
from unittest import mock
import pytest
import builtins


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


# @pytest.fixture
# def mocker():
#    return Time(12, 23, 34)


@pytest.mark.parametrize(
    ('input_time', 'hours', 'minutes', 'seconds'),
    [
        ('12:23:34', 12, 23, 34),
        ('8:20:34', 8, 20, 34),
        ('12:20:10', 12, 20, 10),
        ('13:15:12', 13, 15, 12)
    ]
)
def test_input_time(input_time, hours, minutes, seconds):
    time2 = Time()
    with mock.patch.object(builtins, 'input', lambda: input_time):
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


@pytest.mark.parametrize(
    ('hours', 'minutes', 'seconds', 'result')
    [

    ]
)
def test_init(hours, minutes, seconds):
    pass


@pytest.mark.parametrize(
    ('hours', 'minutes', 'seconds', 'result')
    [

    ]
)
def test_str(hours, minutes, seconds):
    pass

