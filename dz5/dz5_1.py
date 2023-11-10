def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    is_found = False

    while not is_found and low <= high:
        middle = (low + high) // 2
        if lst[middle] == item:
            return lst.index(lst[middle])
        else:
            if item < middle:
                high = middle - 1
            else:
                low = middle + 1


numbs = [x for x in range(1, 20, 1)]
item = float(input("Введите число: "))

print(binary_search(numbs, item))



















