def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_pos = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_pos]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr


data = [-2, 45, 0, 11, -9]
print(selection_sort(data))
