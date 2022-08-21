def insertion_sort(arr):
    key = 0
    j = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    
    return arr

arr = [12, 56, 3, -444, 99, 7, -87324, 99, 0, -7]
print(insertion_sort(arr))