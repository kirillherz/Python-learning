a = [3,2, 8, 1, 3, 5,2,7,4,8,9,4,1,5,3,6,8,6,1,2,4,5,2,1,9]


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
