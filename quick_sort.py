arr = []
def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    right = [x for x in arr if x > pivot]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    return qsort(left) + middle + qsort(right)