import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

count = 0

def dfs(x, y):
    visited[x][y] = True
    if graph[x][y] == '-':
        for r in range(2):
            nx = x + dx[r]
            ny = y + dy[r]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == '-':
                dfs(nx, ny)
    else:
        for r in range(2, 4):
            nx = x + dx[r]
            ny = y + dy[r]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == '|':
                dfs(nx, ny)

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            count += 1
            dfs(i, j)
print(count)
