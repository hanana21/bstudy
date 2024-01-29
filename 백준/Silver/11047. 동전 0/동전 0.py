# 동전0
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)
total = K
count = 0

for coin in coins:
    if total == 0:
        break
    count += total // coin 
    total %= coin
print(count)

