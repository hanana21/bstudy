import sys
from collections import deque

input =sys.stdin.readline
n,m = map(int,input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    indegree[n2] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for g in graph[now]:
            indegree[g] -= 1
            if indegree[g] == 0:
                q.append(g)
    print(*result)
topology_sort()
