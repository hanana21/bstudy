from collections import deque
import sys
input = sys.stdin.readline

n = int(input()) 
INF = int(1e9)
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[INF]*n for _ in range(n)] # 거쳐온 검은 방의 갯수 넣을 거임
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([[x, y]])
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[x][y] < visited[nx][ny]:
                queue.append((nx, ny)) 
                if graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y]
                else:
                    visited[nx][ny] = visited[x][y]+1
    return visited[n-1][n-1]

result = bfs(0, 0)

print(result)
