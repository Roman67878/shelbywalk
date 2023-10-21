def uniq(x):
    if len(x) == len(set(x)):
        return True
    else:
        return False

x = input("Введите строку: ")
print(uniq(x))
