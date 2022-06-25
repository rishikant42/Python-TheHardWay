def bsearch(arr, x):
    low = 0
    high = len(arr) - 1

    while (low <= high):
        mid = (low + high) // 2

        mid_element = arr[mid]

        if mid_element < x:
            low = mid + 1

        elif mid_element > x:
            high = mid - 1
        else:
            return True
    return False


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in range(0, 12):
    print(bsearch(arr, x))
