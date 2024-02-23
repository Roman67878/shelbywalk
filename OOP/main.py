from Time import Time


def main():
    time = Time()
    while True:
        print("1. Ввод времени")
        print("2. Вывод времени")
        print("3. Завершить")
        choise = input("Ваш выбор: ")
        if choise == '1':
            time.input_time()
        elif choise == '2':
            print(time)
        elif choise == "3":
            break


main()