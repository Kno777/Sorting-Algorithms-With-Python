def selection_sort(arr):
    min_ind = 0
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i+1, n):
            if arr[min_ind] > arr[j]:
                min_ind = j
        arr[min_ind], arr[i] = arr[i], arr[min_ind]
    
    return arr

arr = [12, 56, 3, -444, 99, 7, -87324, 99, 0, -7]
print(selection_sort(arr))