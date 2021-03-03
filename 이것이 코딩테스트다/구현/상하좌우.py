# n = int(input())
# plans = input().split()

n = 5
plans = ['R', 'R', 'R', 'U', 'D', 'D']

# x,y 정의
x, y = 1, 1

# L, R, U, D 에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    index = move_types.index(plan)
    next_x = x + dx[index]
    next_y = y + dy[index]

    # 범위를 넘는지 검사한다.
    if next_x > n or next_x < 1 or next_y > n or next_y < 1:
        continue
    else:
        x = next_x
        y = next_y

print(x, y)