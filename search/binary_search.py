def binary_search(arr, num):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return -1


array = [3, 4, 5, 6, 7, 8, 9]
number = 8

result = binary_search(array, number)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
