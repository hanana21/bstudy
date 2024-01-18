import sys
from itertools import combinations

input = sys.stdin.readline
n,s = map(int,input().split())
array = list(map(int,input().split()))
count = 0

for i in range(1,n+1):
    combi = list(combinations(array,i))
    for j in combi:
        if sum(j) == s: count += 1
print(count)

    

