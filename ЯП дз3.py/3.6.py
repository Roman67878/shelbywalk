def simple(a):
    for i in range(2, int((a ** 0.5) + 1)):
        if a % i == 0:
            return ("число составное")
    return ("число простое")
a = int(input("Введите число: "))
print(simple(a))
    
