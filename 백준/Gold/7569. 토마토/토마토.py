# 풀이법: 최소 날짜 구하기=> bfs이용 
#         전체 돌면서 익은 토마토 큐에 삽입하고 안익은것 갯수 확인
#         큐에서 빼면서 범위내,안익은토마토,방문하지 않은 상황이면 visited에 1을 더해준다(하루가 지났다는뜻)
#         그리고 안익은 토마토 갯수(count) -1 해준다. 이미 익은 토마토가 됐으므로 
#         만약 count가 0이면 모두 익었으니 visited에 저장된 가장 마지막 데이터를 뽑아준다.(총 익는데 걸린 일수)
#         count가 0이 아니면 다 익은게 아니니까 -1 출력(문제에서 제시된 상황)
import sys
from collections import deque

input = sys.stdin.readline
M,N,H = map(int,input().split())
graph = [[list(map(int,input().split()))for _ in range(N)] for _ in range(H)]
visited = [[[0]*M for _ in range(N)] for _ in range(H)]

dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    queue = deque()
    cnt = 0
    # 전체 돌면서 큐에 초기 데이터들(익은 토마토) 삽입, 안익은 토마토 개수 세기 
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if graph[h][i][j] == 1:
                    queue.append((h,i,j))
                    visited[h][i][j] = 1
                elif graph[h][i][j] == 0:
                    cnt += 1
    #bfs 시작
    while queue:
        ch,ci,cj=queue.popleft()
        for i in range(6):
            nh = ch+dz[i]
            ni = ci+dx[i]
            nj = cj+dy[i]
            # 범위내, 미방문,안익은 토마토
            if 0<=ni<N and 0<=nj<M and 0<=nh<H and graph[nh][ni][nj]==0 and visited[nh][ni][nj]==0:
                queue.append((nh,ni,nj))
                visited[nh][ni][nj] = visited[ch][ci][cj] + 1 #익은 날짜로 변경
                cnt -= 1 # 이제 익었으니까 안익은 토마토 개수 빼기
    if cnt == 0: #모든 토마토 익었음 => 날짜 출력(처음 익은토마토(출발점)에 1을 넣었기 때문에 -1 해준다)
        return visited[ch][ci][cj] - 1
    else:
        return -1
anser=bfs()
print(anser)