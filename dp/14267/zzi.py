import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 첫 번째 풀이 실패 : 칭찬을 하나 받을 때 마다 dfs()
# 두 번째 풀이 성공 : 칭찬을 한 번에 모아서 dfs()
# 저번에 풀이 2개는 bottom-up, 이번에는 top-down 방식으로 

n,m = map(int,input().split())
superior = list(map(int, input().split()))
compliment = [list(map(int, input().split())) for _ in range(m)]
dp = [0] * (n+1)
visited = [0] * (n+1)

# 후배 리스트
junior = [[] for _ in range(n+1)]

for i in range(n):
    s = superior[i]
    if s != -1:
        junior[s].append(i+1)


def dfs(i):
    visited[i] = 1
    for j in junior[i]:
        if visited[j] == 1:
            continue
        dp[j] += dp[i]
        dfs(j)

for i,w in compliment:
    dp[i] += w
dfs(1)

for i in range(n+1):
    if i == 0:
        continue
    print(dp[i],end = ' ')
