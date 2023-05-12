def linear_search(arr, num):
    for i, n in enumerate(arr):
        if n == num:
            return i
    return False


l = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(l, 11))
