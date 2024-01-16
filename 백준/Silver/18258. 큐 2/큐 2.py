from collections import deque
import sys
queue = deque()
input = sys.stdin.readline
n = int(input())

for i in range(n):
    input_data = input().split()
    if input_data[0] == 'push':
        queue.append(int(input_data[1]))
    elif input_data[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif input_data[0] == 'size':
        print(len(queue))
    elif input_data[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif input_data[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif input_data[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
