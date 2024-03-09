# 숨바꼭질
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start,end):
    q = deque([start])
    visited[start] = 1
    while(q):
        s = q.popleft()
        if(s == end):
            return visited[s] -1
        for i in (s-1,s+1,s*2):
            if  0<= i <= 200000 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[s]+1
                
N,M = map(int,input().split())
visited = [0] *(200001)
result = bfs(N,M)
print(result)
        