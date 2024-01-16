from collections import deque

queue = deque()
n,k = map(int,input().split())

for i in range(1,n+1):
    queue.append(i)
print('<',end='')
while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    print(queue.popleft(),end='')
    if queue:
        print(', ',end='')
print('>')







