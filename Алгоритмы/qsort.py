from datetime import datetime
import random
a = []
for i in range(1, 10000):
    a.append(random.randint(1, 1000))
b = list(a)


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
        if l == r and arr[l] < pivot:
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

def bsort(items):
    for j in range(len(items) - 1,1,-1):
        for i in range(j):
            if items[i] > items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp

start_time = datetime.now()
qsort(a)
end_time = datetime.now()
print(end_time - start_time)
start_time = datetime.now()
bsort(b)
end_time = datetime.now()
print(end_time - start_time)
