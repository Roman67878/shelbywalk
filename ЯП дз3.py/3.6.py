a = int(input("Введите число: "))
k = 0

def simple(a, k):
 for i in range(1, a):
    if (a % i == 0):
        k = k+1
 if (k <= 1):
    print("Число простое")
 else:
    print("Число не является простым")

print(simple(a, k))
  
    