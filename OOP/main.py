from Time import Time, TimeStamp


def main():
    time1 = Time()
    time2 = TimeStamp()
    while True:
        print("1. Ввод времени")
        print("2. Вывод времени")
        print("3. Текущее время")
        print("4. Завершить")
        choise = input("Ваш выбор: ")
        if choise == '1':
            time1.input_time()
        elif choise == '2':
            print(time1)
        elif choise == '3':
            time2.__init__()
            time2.__str__()
        elif choise == '4' or not choise:
            break


main()
