# 탑 
import sys
input = sys.stdin.readline

n = int(input())
top = list(map(int,input().split()))
ans = [0]*n
stack = []

for i in range(n):
    while stack and top[stack[-1]] < top[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1]+1
    stack.append(i)
print(*ans)