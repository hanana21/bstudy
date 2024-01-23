import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(graph,v,visited,group):
    visited[v] = group
    for i in graph[v]:
        if visited[i] == 0:
            result = dfs(graph,i,visited,-group)
            if not result:
                return False
        else:
            if visited[i] == group:
                return False
    return True

k = int(input())
for _ in range(k):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] *(v+1)

    for _ in range(e):
        v1,v2 = map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for i in range(1,v+1):
        if visited[i] == 0:
            result = (dfs(graph,i,visited,1))
            if not result:
                break 

    print('YES') if result else print('NO')