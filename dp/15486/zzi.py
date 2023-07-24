import sys

input = sys.stdin.readline

n = int(input())
consulting =  [list(map(int, input().split())) for _ in range(n)]
max_value = 0
dp = [0 for _ in range(n+1)]

for i in range(1, n + 1):
    t,p = consulting[i-1]
    dp[i] = max(dp[i], dp[i - 1]) 
    if i+t-1 <= n: 
        dp[i+t-1] = max(dp[i+t-1], dp[i-1] + p)

print(max(dp))
