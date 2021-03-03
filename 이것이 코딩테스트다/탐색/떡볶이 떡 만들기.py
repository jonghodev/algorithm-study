h = 6
arr = [20, 15, 10, 17]

start = 0
end = max(arr)
total = 0

result = 0

while start <= end:
    mid = (start + end) // 2

    parsed_arr = [num - mid for num in arr
                  if num > mid]

    total += sum(parsed_arr)

    # 너무 많이 잘랐을 때
    if total >= h:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
    total = 0

print(result)
