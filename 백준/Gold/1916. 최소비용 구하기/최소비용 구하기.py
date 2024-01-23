import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n=int(input())# 노드,간선 
m = int(input()) 
distance = [INF] *(n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) # a->b : c

start,end = map(int,input().split()) #시작점,도착점

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) # 튜플형태로 (길이,노드)저장 길이가 짧은 것 부터 나와야하니까 알아서 해줌
    distance[start] = 0
    while q:
        dist,now =heapq.heappop(q)
        if distance[now] <dist: # 이미 방문한 적 있다면 무시
            continue
        for i in graph[now]:
            cost = dist + i[1] # i는 (도착노드,거리)이런식으로 저장되있음
            if cost < distance[i[0]]: # i[0]는 현재 노드=> 현재 노드에 저장된 값이랑 새로운 값더하기 
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
print(distance[end])
