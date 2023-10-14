def average(numb):
    return sum(numb) / len(numb)

numb = []
n = int(input("введите желаемую длину списка: "))
for i in range(1, n+1):
    numb.append(i)
print(numb)

average(numb)
print(average(numb))
