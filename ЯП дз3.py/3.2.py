def kalendar(n):
    if n == 12 or n <= 2:
        print("зима")
    elif n <= 5:
        print("весна")
    elif n <= 9:
        print("лето")
    else:
        print("осень")

n = int(input("введите число от 1 до 12: "))

kalendar(n)
