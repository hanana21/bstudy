# 동전 
T = int(input())
for _ in range(T):
    N = int(input())
    coins = [0] + list(map(int,input().split()))
    M = int(input())
    dp = [[0]*(M+1) for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(N+1):
        for j in range(M+1):
            if coins[i] <= j:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
            else:
                dp[i][j] = dp[i-1][j] 
    print(dp[-1][-1])

