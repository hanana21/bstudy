from collections import deque

def solution():
    n = int(input()) #보드의 크기
    a = int(input()) #사과의 갯수
    apples = [tuple(map(int, input().split())) for _ in range(a)]  # 사과의 위치
    d = int(input()) # 방향변환 횟수
    directions = [input().split() for _ in range(d)]  # 방향 변환 정보

    # 초기 설정 
    board = [[0] * (n + 1) for _ in range(n + 1)]  # 1부터 시작하기 위해 (n+1) x (n+1) 크기의 보드 생성
    for apple in apples:
        board[apple[0]][apple[1]] = 1  # 사과의 위치 표시

    snake = deque([(1, 1)])  # 뱀의 초기 위치
    x,y,direction = 1,1,0  # 뱀위치,초기 방향
    time = 0
    direction_index = 0 # 방향 변환 정보를 처리할 인덱스

    # ehdqnrtjska
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while True:
        time += 1
        # 다음 위치 계산
        x += dx[direction]
        y += dy[direction]

        # 벽 또는 자기 자신에 부딪히면 게임 종료
        if x < 1 or x > n or y < 1 or y > n or (x, y) in snake:
            break
        # 뱀의 머리를 추가
        snake.append((x, y))

        # 사과가 있는 경우
        if board[x][y] == 1:
            board[x][y] = 0  # 사과를 먹었으므로 해당 칸을 비워줌
        else:
            # 사과가 없는 경우, 꼬리 제거
            snake.popleft()

        # 방향 변환 정보가 있고, 해당 시간에 방향을 바꿀 때
        if direction_index < d and time == int(directions[direction_index][0]):
            command = directions[direction_index][1]
            if command == 'L':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
            direction_index += 1

    print(time)

# 함수 호출
solution()



