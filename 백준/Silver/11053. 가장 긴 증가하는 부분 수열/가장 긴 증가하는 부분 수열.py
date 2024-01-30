# 가장 긴 증가하는 부분 수열 
N = int(input())
A = [0]+list(map(int,input().split()))
dp = [0]*(N+1)

for i in range(1,N+1):
    mx = 0
    for j in range(i):
        if A[i] > A[j]:
            mx = max(mx,dp[j])
    dp[i] = mx+1
print(max(dp))
