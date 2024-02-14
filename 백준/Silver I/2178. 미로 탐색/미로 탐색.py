from collections import deque
# N,M에 도달하는 최단 경로 
N,M = map(int,input().split())
graph = [list(map(int,input())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
directions = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs(graph,sx,sy,visited):
    q = deque([(sx,sy)])
    visited[sx][sy] = True
    while(q):
        x,y = q.popleft()
        for d in directions:
            nx = x+d[0]
            ny = y+d[1]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and graph[nx][ny]==1:
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] =True

bfs(graph,0,0,visited)
print(graph[N-1][M-1])
