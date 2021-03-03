def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)


array = [5, 1, 6, 8, 10, 24, 999, 1042, 7783]

array.sort()

print(binary_search(array, 999, 0, len(array) - 1))
