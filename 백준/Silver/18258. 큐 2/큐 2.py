# 큐 2
import sys
from collections import deque
input = sys.stdin.readline
d = deque()

def push(data):
    d.append(data)

def pop():
    if not d:
        print(-1)
    else:
        front = d.popleft()
        print(front)

def size():
    print(len(d))

def empty():
    if not d:
        print(1)
    else:
        print(0)

def front():
    if not d:
        print(-1)
    else:
        print(d[0])

def back():
    if not d:
        print(-1)
    else:
        print(d[-1])


N = int(input())
for _ in range(N):
    order = input().split()
    if order[0] == 'push':
        push(order[1])
    elif order[0] == 'pop':
        pop()
    elif order[0] == 'size':
        size()
    elif order[0] == 'empty':
        empty()
    elif order[0] == 'front':
        front()
    else:
        back()