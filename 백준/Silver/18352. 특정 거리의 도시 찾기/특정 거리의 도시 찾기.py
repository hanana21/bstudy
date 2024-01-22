import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append((n2, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(x)

result = [i for i in range(1, n + 1) if distance[i] == k]
result.sort()
if result:
    for r in result:
        print(r)
else:
    print(-1)
