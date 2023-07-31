import sys
sys.setrecursionlimit(10 ** 9)
n = int(sys.stdin.readline())
c = [[] for i in range(n+1)]
dp = [[0,0] for i in range(n+1)]

for _ in range(n-1):
    a,b = map(int , sys.stdin.readline().split(" "))
    # 양방향
    c[a].append(b)
    c[b].append(a)

visited = [0 for _ in range(n+1)]

def dfs(start):
    global c
    global visited
    if len(c[start]) ==0:
        dp[start][1] = 1
        dp[start][0] = 0
    else:
        for i in c[start]:
            if visited[i] == 0:
                dfs(i)
                # 재귀 동작
                dp[i][1] = min(dp[i][1], dp[i][0])
                dp[i][0] += dp[start][1]
        dp[start][1] += 1

dfs(1)
print(min(dp[1][0], dp[1][1]))
