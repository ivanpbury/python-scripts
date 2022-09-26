def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list)-1

    if high < low:
        return -1
    mid = (low+high) // 2
   
    if list[mid] == target:
        return mid
    elif list[mid] > target:
        return binary_search(list, target, low, mid-1)
    elif list[mid] < target:
        return binary_search(list, target, mid+1, high)

    return -1

list = [1, 2, 3, 6, 8, 10, 11]

print(binary_search(list, 11))