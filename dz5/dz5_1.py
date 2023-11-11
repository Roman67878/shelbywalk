def binary_search(lst, item):
    
    low = 0
    high = len(lst) - 1

    while low <= high:
        middle = (low + high) // 2
        if lst[middle] == item:
            return middle
        if item < middle:
            high = middle - 1
        else:
            low = middle + 1


numbs = [1,1,1,4,5,6,7]
item = float(input("Введите число: "))

print(binary_search(numbs, item))
















