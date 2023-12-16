def Stallone(lst):
    i = 0
    el = lst[0]
    s = len(lst)
    while i < len(lst) and len(lst) > 0:
        if el <= lst[i]:
            el = lst[i]
            i += 1
        else:
            del lst[i]
            s -= 1
    return lst


nums = [10, 23, 5, 67, 31]
new_nums = Stallone(nums)
print(new_nums)