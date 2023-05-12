# Like the binary search, it also separates the lists into sub-lists. This procedure divides the list into three parts
# using two intermediate mid-values. As the lists are divided into more subdivisions, so it reduces the time to search
# a key value.

def ternarySearch(low, high, key, arr):
    while high >= low:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        if key == arr[mid1]:
            return mid1
        if key == arr[mid2]:
            return mid2
        if key < arr[mid1]:
            high = mid1 - 1
        elif key > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2
    return -1


array = [10, 20, 30, 50, 70, 80, 100, 110]
idx = ternarySearch(0, len(array), 30, array)
print(110, "found at", idx)
