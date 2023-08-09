import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
w,h = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(h)]


dx = [0,1,0,-1]
dy = [1,0,-1,0]

hx = [-1,-2,-2,-1,2,1,1,2]
hy = [-2,-1,1,2,1,2,-2,-1]
INF = 10000000
ans = INF
visited = [[[0] * (n + 1) for _ in range(w)] for _ in range(h)]


q = deque()
q.append((0,0,0,0))
visited[0][0][0] = 1


while len(q) > 0:
    x,y,count,h_count = q.popleft()


    if x == h-1 and y == w-1:
        ans = min(ans,count)
    
    if h_count < n:
        # 말처럼 움직이기
        for i in range(8):
            nx = x + hx[i]
            ny = y + hy[i]
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 0 and visited[nx][ny][h_count+1] == 0:
                visited[nx][ny][h_count+1] = 1
                q.append((nx,ny,count+1,h_count+1))

    # 인접 움직이기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 0 and visited[nx][ny][h_count] == 0:
            visited[nx][ny][h_count] = 1
            q.append((nx,ny,count+1,h_count))


if ans == INF:
    print(-1)
else:
    print(ans)
