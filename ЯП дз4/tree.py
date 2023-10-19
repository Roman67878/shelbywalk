def uniq(x):
    if len(x) == len(set(x)):
        return True
    else:
        return False

x = input("Введите строку: ")
print(uniq(x))

if __name__ == '__main__':
    print(uniq(input()))