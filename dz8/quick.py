def quick(lst):
    low = []
    high = []
    middle = (len(lst) // 2)
    for i in lst:
        if i > middle:
            high.append(i)
        else:
            low.append(i)
    return low, middle, high


nums = [2, 1, 3, 4, 5]
new_nums = quick(nums)
print(new_nums)



