node = int(input())
edge = int(input())
graph = [[] for _ in range(node+1)]
visited = [False] * (node+1)
count = 0

for i in range(edge):
    node1,node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

def dfs(graph,v,visited):
    global count
    visited[v] = True
    count += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
dfs(graph,1,visited)
print(count-1)


    