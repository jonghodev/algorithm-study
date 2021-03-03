# Input Values
row = 4
column = 4
x = 1
y = 1
direction = 0
array = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * column for _ in range(row)]

# 현재 좌표 방문처리
d[x][y] = 1

# 0: 북, 1: 동, 2: 남, 3: 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
countVal = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()

    next_x = x + dx[direction]
    next_y = y + dy[direction]

    # 회전한 이후 정면에 가보지 않는 칸이 있다면 전진
    if d[next_x][next_y] == 0 and array[next_x][next_y] == 0:
        d[next_x][next_y] = 1
        x = next_x
        y = next_y

        countVal += 1
        turn_time = 0
        continue
    # 회전한 이후, 가본 땅이거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        next_x = x - dx[direction]
        next_y = y - dy[direction]

        # 뒤로 갈 수 있다면 이동하기
        if array[next_x][next_y] == 0:
            x = next_x
            y = next_y
        # 뒤로 이동할 수 없다면 끝내기
        else:
            break
        turn_time = 0

print(countVal)
