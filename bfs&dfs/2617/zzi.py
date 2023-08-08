import sys

input = sys.stdin.readline

n,m = map(int,input().split())
marble = [list(map(int, input().split())) for _ in range(m)]

light = [[] for _ in range(n+1)]
heavy = [[] for _ in range(n+1)]
ans = 0

for x,y in marble:
    light[x].append(y)
    heavy[y].append(x)

def search_light(v):
    if light_visited.count(1) >= (n // 2) + 1:
        return 
    for l in light[v]:
        if light_visited[l] == 0:
            light_visited[l] = 1
            search_light(l)


def search_heavy(v):
    if heavy_visited.count(1) >= (n // 2) + 1:
        return
    for l in heavy[v]:
        if heavy_visited[l] == 0:
            heavy_visited[l] = 1
            search_heavy(l)


for i in range(1,n+1):
    light_visited = [0] * (n+1)
    heavy_visited = [0] * (n+1)
    mid = (n // 2) + 1
    search_light(i)
    search_heavy(i)
    if light_visited.count(1) >= mid or heavy_visited.count(1) >= mid:
        ans += 1

print(ans)


# 중간 구슬이 절대 될 수 없는 것 => 큰것이 (n//2 + 1)개 이상 있거나 작은것이 (n//2 + 1)개 이상 있으면 
