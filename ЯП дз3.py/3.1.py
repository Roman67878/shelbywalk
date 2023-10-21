def spisok():
    x = []
    while True:
        y = input("введите число ")
        if not y:
            break
        x.append(y)
    return x

print(spisok())
