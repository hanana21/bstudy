import sys
sys.setrecursionlimit(100000) 
input = sys.stdin.readline

node,edge = map(int,input().split())
graph = [[] for i in range(node+1)]
visited = [False] * (node+1)

for i in range(edge):
    node1,node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

def dfs(graph,v,visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)   
count = 0
for i in range(1,node+1):
    if not visited[i]:
        dfs(graph,i,visited)
        count += 1
print(count)

