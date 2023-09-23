a = float(input("введите первое число "))
b = float(input("введите второе число "))
c = float(input("введите третье число "))
d = float(input("введите четвертое число "))
f = float(input("введите пятое число "))
try:
    g = (a * b - c)/(d - f)
except ZeroDivisionError:
    print("на 0 делить нельзя!")
print(g)