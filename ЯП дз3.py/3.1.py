def spisok(x):
    y = input("введите число ")
    while y:
     x.append(y)
     y = input("введите число ")
    print(x)

x = []

spisok(x)
