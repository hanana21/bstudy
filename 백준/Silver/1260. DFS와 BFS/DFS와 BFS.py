from collections import deque

n,e,start = map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(e):
    node1,node2=map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

visited = [False] * (n+1)

def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] =True

dfs(graph,start,visited)
visited = [False] * (n+1)
print()
bfs(graph,start,visited)



