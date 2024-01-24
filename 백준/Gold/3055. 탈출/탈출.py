import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque()
    bx, by = 0, 0
    # 큐 입력값 받기
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'S':
                q.append((i, j))
            elif graph[i][j] == 'D':
                bx, by = i, j      
    for i in range(R):
        for j in range(C):
            if graph[i][j] == '*':
                q.append((i, j))   
    # bfs 동작
    while q:
        x, y = q.popleft()
        if x == bx and y == by:  # 종료 조건: 비버집 도착시
            return visited[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C :  # 만약 범위 안이라면 
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    visited[nx][ny] = visited[x][y] + 1 
                    graph[nx][ny] = 'S' 
                    q.append((nx, ny))   
                elif (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[x][y] == '*':
                    graph[nx][ny] = '*'
                    q.append((nx, ny)) 
    return 'KAKTUS'

answer = bfs()
print(answer)
