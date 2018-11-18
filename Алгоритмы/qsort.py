a = []
import random
for i in range(1,100):
    a.append(random.randint(1,100))

def partition(arr, l, r):
    pivot = arr[r]
    while l < r:
        while (arr[l] < pivot):
            l += 1
        while arr[r] > pivot:
            r -= 1
        if l < r:
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
            r -= 1
            l += 1
        if l == r and  arr[l] < pivot:
            l += 1
    return l


def _qsort(arr, l, r):
    i = partition(arr, l, r)
    if l < (i - 1):
        _qsort(arr, l, i-1)
    if i < r:
        _qsort(arr, i, r)


def qsort(items):
    _qsort(items, 0, len(items)-1)


qsort(a)
