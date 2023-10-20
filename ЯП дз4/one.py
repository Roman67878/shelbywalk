def spisok(x):
    lst = []
    while True:
        y = int(input("Введите число: "))
        lst.append(y)
        if not y:
            break
        return lst
def sdwig(x, b):
    b %= len(x)
    return x[-b:] + x[:-b]
