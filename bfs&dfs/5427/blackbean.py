from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def burn():
    for _ in range(len(fire)):
        x, y = fire.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] != '#' and arr[nx][ny] != '*':
                    arr[nx][ny] = '*'
                    fire.append((nx, ny))


def move():
    isgo = False
    for _ in range(len(start)):
        x, y = start.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and arr[nx][ny] != '#' and arr[nx][ny] != '*':
                    isgo = True
                    visited[nx][ny] = visited[x][y] + 1
                    start.append((nx, ny))
            else:
                return visited[x][y]
    if not isgo:
        return 'IMPOSSIBLE'


T = int(input())
for _ in range(T):
    M, N = map(int, input().split())
    arr = []
    fire = deque()
    start = deque()
    for i in range(N):
        arr.append(list(input().strip()))
        for j in range(M):
            if arr[i][j] == '*':
                fire.append((i, j))
            if arr[i][j] == '@':
                start.append((i, j))
    visited = [[0] * M for _ in range(N)]
    visited[start[0][0]][start[0][1]] = 1

    result = 0
    while True:
        burn()
        result = move()
        if result:
            break

    print(result)