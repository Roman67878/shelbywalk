def fib(n):
    x = [0, 1]
    for _ in range(n):
        x.append(x[-1] + x[-2])
    return x[:n]

n = int(input("введите число "))

print(fib(n))

