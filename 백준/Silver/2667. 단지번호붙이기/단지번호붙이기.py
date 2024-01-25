import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [0, 0, 1, -1] #오,왼,위,아래
dy = [1, -1, 0, 0]

def dfs(x, y,count_house):
    visited[x][y] = True
    count_house += 1
    for r in range(4):
        nx = x + dx[r]
        ny = y + dy[r]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 1:
            count_house = dfs(nx, ny, count_house) 
    return count_house

count_group= 0
count_house=[]
for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            count_group += 1
            result = dfs(i, j, 0)
            count_house.append(result)

print(count_group)
count_house.sort()
print(*count_house, sep='\n')

