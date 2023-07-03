import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx, dy = [-1,1,0,0],[0,0,-1,1]
q = deque()
day = 0
check = False

def bfs(a,b):
    q.append((a,b))
    while q:
        x,y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif graph[nx][ny] == 0:
                    count[x][y] += 1
    return 1

while True:
    visited = [[False] * m for _ in range(n)]
    count = [[0] * m for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i,j))
    # 빙산을 깍아줌
    for i in range(n):
        for j in range(m):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    if len(result) == 0:
        break
    if len(result) >= 2:
        check = True
        break
    day += 1
if check:
    print(day)
else:
    print(0)