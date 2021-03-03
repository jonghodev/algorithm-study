n = int(input())
input_arr = [[]] * n

for i in range(n):
    input_arr[i] = list(map(int, input().split()))

d = [[0] * i for i in range(1, n + 1)]
d[0][0] = input_arr[0][0]

for i in range(1, len(input_arr)):
    for j in range(len(input_arr[i])):
        up = d[i - 1][j] if j != len(d[i]) - 1 else 0
        left_up = d[i - 1][j - 1] if j > 0 else 0
        target = input_arr[i][j] + max(up, left_up)
        d[i][j] = max(d[i][j], target)

answer = max(d[len(input_arr) - 1])

print(answer)
