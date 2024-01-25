import sys
from collections import deque

input = sys.stdin.readline
N,K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
S,X,Y = map(int,input().split())

visited = [[0] * N for _ in range(N)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
virus = []

def bfs():
    # 큐에 넣기
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                virus.append((graph[i][j],i,j,0))
                visited[i][j] = graph[i][j]
    virus.sort()
    q = deque(virus) 

    # bfs진행
    while q:
        virus_type , x , y, times= q.popleft()
        if times == S:
            break
        for r in range(4):
            nx = x+dx[r]
            ny = y+dy[r]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                q.append((virus_type,nx,ny,times+1))
                visited[nx][ny] = virus_type
# 결과 출력
bfs() 
print(visited[X-1][Y-1])



