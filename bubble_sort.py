def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [12, 56, 3, -444, 99, 7, -87324, 99, 0, -7]
print(bubble_sort(arr))
