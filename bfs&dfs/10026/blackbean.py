from collections import deque

n = int(input())

data = []

graph_R = []
graph_G = []
graph_B = []

visit = [[0] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, color):
    if visit[x][y] == 1:
        return 0
    visit[x][y] = 1
    queue = deque()
    queue.append((x, y))
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if data[nx][ny] == color:
                    visit[nx][ny] = 1
                    queue.append((nx, ny))
                else:
                    continue
    return 1


for i in range(n):
    data.append(input())
    for j in range(n):
        if data[i][j] == 'R':
            graph_R.append((i, j))
        elif data[i][j] == 'G':
            graph_G.append((i, j))
        elif data[i][j] == 'B':
            graph_B.append((i, j))

# 적록색맹이 아닌 경우
area_yes = 0
# 적록색맹인 경우
area_no = 0
# 각 영역의 크기
area_R, area_G, area_B = 0, 0, 0

# 빨간색
for x, y in graph_R:
    area_R += bfs(x, y, 'R')

# 초록색
for x, y in graph_G:
    area_G += bfs(x, y, 'G')
# 파란색
for x, y in graph_B:
    area_B += bfs(x, y, 'B')

area_yes += area_R + area_G + area_B
# 빨강 파랑만 방문 여부 초기화
visit = [[0] * n for _ in range(n)]

for x, y in graph_B:
    visit[x][y] = 1

# 방문 맵을 R -> G
for i in range(n):
    data[i] = data[i].replace('G', 'R')

graph_R = graph_R + graph_G

for x, y in graph_R:
    area_no += bfs(x, y, 'R')
area_no += area_B



print(area_yes, end=' ')
print(area_no)
