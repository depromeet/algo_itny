import sys

input = sys.stdin.readline

t, w = map(int,input().split())
plum = []
for i in range(t):
    plum.append(int(input()))

dp = [[0]*(w+1) for _ in range(t)]

for i in range(t):
    for j in range(w+1):
        if j == 0:
            if plum[i] == 1:
                dp[i][j] = dp[i-1][j] + 1
            else:
                dp[i][j] = dp[i-1][j]
        else:
            if (j % 2 == 1 and plum[i] == 2) or  (j % 2 == 0 and plum[i] == 1):
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + 1
            else:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])
            
print(max(dp[t-1]))
