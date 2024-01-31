# 계단 오르기 
n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)
dp[1] = stairs[1]

for i in range(2,n+1):
    dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i],dp[i-2]+stairs[i])
print(dp[n])