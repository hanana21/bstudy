N = int(input())
graph = [list(map(int,input())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
directions = [(0,1),(-1,0),(0,-1),(1,0)]
cnt = 0
anser = []

def dfs(graph,x,y,visited,count):
    count += 1
    visited[x][y] = True
    for i in directions:
        nx = x + i[0]
        ny = y + i[1]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and graph[nx][ny] == 1:
            count = dfs(graph,nx,ny,visited,count)
    return count

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            cnt += 1
            anser.append(dfs(graph,i,j,visited,0))
print(cnt)
anser.sort()
print(*anser, sep='\n')