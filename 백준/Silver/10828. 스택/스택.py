# 스택 
import sys
input = sys.stdin.readline
s = []

def push(num):
    s.append(num)

def pop():
    if not s:
        print(-1)
    else:
        outdata = s.pop()
        print(outdata)

def size():
    print(len(s))

def empty():
    if not s:
        print(1)
    else:
        print(0)

def top():
    if not s:
        print(-1)
    else:
        print(s[-1])


N = int(input())

for _ in range(N):
    data = input().split()
    order = data[0]
    num = 0
    if len(data) == 2:
        num = int(data[1])

    if order == 'push':
        push(num)
    elif order == 'pop':
        pop()
    elif order == 'size':
        size()
    elif order == 'empty':
        empty()
    else:
        top()





