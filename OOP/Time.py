import datetime
from math import fabs


class TimeValueError(ValueError):
    def __init__(self, message="", information=""):
        self.message = message
        self.information = information


class Time:
    def __init__(self, hours=1, minutes=1, seconds=1):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def input_time(self):
        time_input = input("Введите время в формате Час : Минуты : Секунды: ")
        self.hours, self.minutes, self.seconds = map(int, time_input.split(":"))
        self.validate()

    def __str__(self):
        return f"Время: {self.hours}:{self.minutes}:{self.seconds}"

    def validate(self):
        if self.hours not in range(24) or self.minutes not in range(60) or self.seconds not in range(60):
            raise TimeValueError('Неправильные данные')

    def __add__(self, other):
        sum_time = Time(hours=self.hours + other.hours,
                        minutes=self.minutes + other.minutes,
                        seconds=self.seconds + other.seconds)

        if (self.seconds + other.seconds) >= 60:
            sum_time.minutes += 1
            sum_time.seconds -= 60

        if sum_time.minutes >= 60:
            sum_time.hours += 1
            sum_time.minutes -= 60

        if sum_time.hours >= 24:
            sum_time.hours -= 24

        return sum_time

    def __sub__(self, other):
        delta_time = Time(hours=self.hours - other.hours,
                          minutes=self.minutes - other.minutes,
                          seconds=self.seconds - other.seconds)

        if delta_time.seconds < 0:
            delta_time.minutes -= 1
            delta_time.seconds += 60
            if other.seconds > self.seconds:
                delta_time.seconds = abs(other.seconds - self.seconds)

        if delta_time.minutes < 0:
            delta_time.hours -= 1
            delta_time.minutes += 60
            if self.minutes - other.minutes:
                delta_time.minutes = abs(other.minutes - self.minutes)

        if delta_time.hours < 0:
            raise TimeValueError('Неверный результат вычитания')

        return delta_time

    def __eq__(self, other):
        if isinstance(other, Time):
            return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds
        else:
            raise TimeValueError('Нельзя провести операцию')


class TimeStamp(Time):
    def __init__(self):
        current = datetime.datetime.now()
        super().__init__(current.hour, current.minute, current.second)


time1 = Time(23, 58, 58)
time2 = Time(4, 23, 55)
time3 = Time(18, 34, 56)
time4 = Time(17, 43, 43)
time1 = time1.__add__(time2)
time3 = time3.__sub__(time4)
print(time1)
print(time3)
time5 = TimeStamp()
print(time5)
