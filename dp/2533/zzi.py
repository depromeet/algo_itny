# 1 -> 2,3,4
# 2 -> 1,5,6
# 3 -> 1
# 4 -> 1,7,8
# 5 -> 2
# 6 -> 2
# 7 -> 4
# 8 -> 4
import sys

input = sys.stdin.readline

n = int(input())
tree = []
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
dp= [[0,1] for _ in range(n+1)] # 얼리어답터가 아닌 경우, 얼리어답터인경우

while True:
    r = list(map(int, input().split()))
    if len(r) == 0:
        break
    tree.append(r)

for [a,b] in tree:
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    visited[v]=True 
    for next in graph[v]: 
        if(visited[next]): continue 
        dfs(next)
        dp[v][0]+=dp[next][1] 
        dp[v][1]+=min(dp[next])
    
    # print(v,dp)

dfs(1)
print(min(dp[1]))
