x = []
y = input("введите число ")
while y:
    y = input("введите число ")
    x.append(y)
    x.sort(reverse=True)
print("".join(x))
