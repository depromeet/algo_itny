from collections import deque

import sys
from collections import deque

m, n, h = map(int, input().split())
tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
ans = 0
queue = deque()

for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato[z][x][y] == 1:
                queue.append((x,y,z))

dx = [0,1,0,-1]
dy = [1,0,-1,0]
dz = [-1,1]

while len(queue):
    x,y,z = queue.popleft()
    print(tomato)
    #  위, 아래, 왼쪽, 오른쪽
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z
        if 0 <= nx < n and 0 <= ny < m and tomato[z][x][y] >= 1 and tomato[nz][nx][ny] == 0:
            tomato[nz][nx][ny] = tomato[z][x][y] + 1
            queue.append((nx,ny,nz))
    # 앞, 뒤
    for i in range(2):
        nx = x
        ny = y
        nz = z + dz[i]
        if 0 <= nz < h and tomato[z][x][y] >= 1 and tomato[nz][nx][ny] == 0: 
            tomato[nz][nx][ny] = tomato[z][x][y] + 1
            queue.append((nx,ny,nz))

for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato[z][x][y] == 0:
                ans = -1
                break
            else:
                ans = max(ans,tomato[z][x][y]-1)
        if ans == -1:
            break
    if ans == -1:
        break

print(ans)
