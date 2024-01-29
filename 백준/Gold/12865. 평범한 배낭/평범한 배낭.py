import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]
items = [(0, 0)]

for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= items[i][0]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i][0]] + items[i][1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][K])
