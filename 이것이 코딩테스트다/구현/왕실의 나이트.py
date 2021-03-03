row = 1
column = 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, 1), (-2, -1), (1, -2), (-1, -2), (2, 1), (2, -1), (1, 2), (1, -2)]

result = 0

# 8가지 방향에 대하여 이동이 가능한지 확인
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)