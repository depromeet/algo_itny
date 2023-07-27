import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,r,q = map(int,input().split())
nodes = [list(map(int, input().split())) for _ in range(n-1)]
sub = []
for _ in range(q):
    sub.append(int(input()))

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
dp = [1] * (n+1)

for u,v in nodes:
    graph[v].append(u)
    graph[u].append(v)


def dfs(x):
    visited[x] = 1
    for node in graph[x]:
        if visited[node] == 1:
            continue
        dfs(node)
        dp[x] += dp[node]

visited[r] = 1
dfs(r)
for s in sub:
    print(dp[s])
