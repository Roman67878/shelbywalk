import datetime

class Time:
    def __init__(self, hours=1, minutes=1, seconds=1):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def input_time(self):
        while True:
            time_input = input("Введите время в формате Час : Минуты : Секунды: ")
            self.hours, self.minutes, self.seconds = map(int, time_input.split(":"))
            if self.hours not in range(24) or self.minutes not in range(60) or self.seconds not in range(60):
                print("Некорректный ввод")
            else:
                break

    def __str__(self):
        return f"Время: {self.hours}:{self.minutes}:{self.seconds}"


class TimeStamp(Time):
    def __init__(self):
        super().__init__()
        current_time = datetime.datetime.now()
        self.hours = current_time.hour
        self.minutes = current_time.minute
        self.seconds = current_time.second

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"


timestamp = TimeStamp()
print(timestamp)

