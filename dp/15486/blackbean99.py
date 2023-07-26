n = int(input())

time, p = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    time[i], p[i] = map(int, input().split())

dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])  # 이전까지의 최댓값 (어제의 최댓값과 오늘의 최댓 값을 비교해야 한다)
    target = i + time[i] - 1  # 당일 포함
    if target <= n:  # n일 전에만 계산한다
        dp[target] = max(dp[target], dp[i] + p[i])
        # dp[i] + p[i]
print(max(dp))