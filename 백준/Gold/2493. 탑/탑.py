# 탑 
import sys
input = sys.stdin.readline

n = int(input())
top = list(map(int,input().split()))
ans = [0]*n
stack = []

for i in range(n):
    while stack and stack[-1][0] < top[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1][1]
    stack.append([top[i],i+1])

print(*ans)