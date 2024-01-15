import sys
input=sys.stdin.readline
n=int(input())
array = [int(input()) for i in range(n)]
result = sorted(array)
for i in result:
    print(i)