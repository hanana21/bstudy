from collections import deque

n, m = map(int, input().split())
graph = [list(map(int,input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([[x, y]])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]==1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + graph[nx][ny]
    return graph[n-1][m-1]

print(bfs(0, 0))
