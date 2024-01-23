import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

anser = 0

n = int(input())
graph = [[] for _ in range(n+1)]
location = [0] + list(map(int,input().strip()))
visited= [False] * (n+1)

for _ in range(n-1):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    if location[n1] == 1 and location[n2] == 1:
        anser += 2

def dfs(graph,v,visited):
    inside_count = 0
    visited[v] = True
    for i in graph[v]:
        if location[i] == 1:
            inside_count += 1
        elif not visited[i] and location[i] == 0 :
            dfs(graph,i,visited)
    return inside_count

for i in range(1,n+1):
    if location[i] == 0 and not visited[i]:
        result = dfs(graph,i,visited)
        anser += result*(result-1)

print(anser)