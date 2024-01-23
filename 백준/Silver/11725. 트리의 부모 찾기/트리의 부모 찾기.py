import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) 

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
visited = [False] * (n+1)
result = [0]*(n+1)

def dfs(graph,v,visited):
    visited[v] = True
    for i in sorted(graph[v]):
        if not visited[i]:
            visited[i] = True
            result[i] =v
            dfs(graph,i,visited)  
dfs(graph,1,visited)
for i in range(2,n+1):
    print(result[i])

