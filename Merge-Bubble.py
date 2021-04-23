def mergesort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(lst_1, lst_2):
    ret = []
    while lst_1 and lst_2:
        if lst_1[0] < lst_2[0]:
            ret.append(lst_1.pop(0))
        else:
            ret.append(lst_2.pop(0))
    ret.extend(lst_1)
    ret.extend(lst_2)
    return ret

# ------- TEST CASES ------- #

print(mergesort([9,3,1,5,6,1,3]))

print(mergesort([10,6,4,2,1]))

print(mergesort([8123, 1236712, 5347, 81231, 12391]))