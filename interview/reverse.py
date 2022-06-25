def reverse_arr1(arr):
    if not arr:
        return []
    return [arr[-1]] + reverse_arr1(arr[:len(arr)-1])


def reverse_arr2(arr):
    if not arr:
        return []
    return [arr.pop()] + reverse_arr2(arr)


def reverse_arr3(arr, count):
    if not count:
        return []
    return [arr[count-1]] + reverse_arr3(arr[:count-1], count-1)


def reverse_str1(s):
    if not s:
        return ""
    return s[-1] + reverse_str1(s[:len(s)-1])


def reverse_str2(s, n):
    if n == 0:
        return ""
    return s[n-1] + reverse_str2(s[:n-1], n-1)


print(reverse_arr2([1, 2, 3, 4, 5]))
print(reverse_arr3([1, 2, 3, 4, 5], 5))

print(reverse_str1("hello"))
print(reverse_str2("hello", 5))
