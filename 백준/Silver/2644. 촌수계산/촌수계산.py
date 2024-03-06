#촌수 계산하기 
from collections import deque

N = int(input())
start, end = map(int,input().split())
D = int(input())

graph = [[] for _ in range(N+1)]
for i in range(D):
    p,c = map(int,input().split())
    graph[p].append(c)
    graph[c].append(p)

visited = [0]*(N+1)

def bfs(start,end):
    q = deque([start])
    visited[start] = 1
    while(q):
        parent = q.popleft()
        if parent == end:
            return visited[end] -1
        for i in graph[parent]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[parent]+1
    return -1
result = bfs(start,end)
print(result)