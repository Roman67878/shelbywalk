def fac(x):   
    y = 1
    for i in range(1, x+1):
        y *= i
        i -= 1
    return y

x = int(input("Введите число: "))
print(fac(x))