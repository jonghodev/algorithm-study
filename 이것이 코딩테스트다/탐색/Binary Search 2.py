def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


array = [5, 1, 6, 8, 10, 24, 999, 1042, 7783]

array.sort()

print(binary_search(array, 999, 0, len(array) - 1))
