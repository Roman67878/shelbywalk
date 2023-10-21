def average(numb):
    return sum(numb) / len(numb)

n = [int(n) for n in input().split()]
print(average(n))
