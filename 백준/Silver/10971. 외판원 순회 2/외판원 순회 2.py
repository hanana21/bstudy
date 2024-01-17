n = int(input())
map = [list(map(int,input().split())) for _ in range(n)]
visited = [0] * n
anser = 999999999

def search(start,now,costsum):
    global anser
    if costsum > anser: # 답보다 크면 신경쓸 가치도 없다 나가기
        return
    if start == now and 0 not in visited: # 제자리도착,모두 방문 => 지금합이 지금답보다 작으면 저장
        if costsum < anser:
            anser = costsum
        return  
    for i in range(n):
        if map[now][i] != 0 and visited[i] == 0:
            visited[i] = 1
            search(start,i,costsum+map[now][i])
            visited[i] = 0
search(0,0,0)
print(anser)