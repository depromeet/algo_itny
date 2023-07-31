import sys 

n,m = map(int,sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(int(input()))

mn = 2000000000

graph.sort()

for st in range(n):
    en = 0
    while en < n and graph[en] - graph[st] < m:
        en += 1
    if en == n:
        break
    mn = min(mn,graph[en] - graph[st])
print(mn)
