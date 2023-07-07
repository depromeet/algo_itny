# 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
# 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
from collections import deque

n = int(input())

x ,y, shark_size = 0, 0, 2

graph = []

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] == 9:
            x,y = i,j

def bfs(x,y,size):
    distance = [[0]*n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다. (bfs사용)
    q = deque()
    q.append((x,y))

    visited[x][y] = 1
    temp = []
    while q:
        current_x, current_y = q.popleft()
        for i in range(4):
            nx = current_x + dx[i]
            ny = current_y + dy[i]
            if 0<= nx < n and 0<= ny < n and visited[nx][ny] == 0:
                # 상어 크기보다 작으면
                if graph[nx][ny] <= size:
                    q.append((nx,ny))
                    # 방문처리
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[current_x][current_y] + 1
                    if graph[nx][ny] < size and graph[nx][ny] != 0:
                        temp.append((nx,ny,distance[nx][ny]))

# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
#     sorted 내림차순 정렬
    return sorted(temp,key=lambda x: (-x[2],-x[0],-x[1]))


result = 0
cnt = 0
while 1:
    shark = bfs(x,y,shark_size)
    # 엄마를 부르는 경우
    if len(shark) == 0:
        break
    # 거리가 가까운 물고기가 많은 경우
    nx,ny,dist = shark.pop()
    # 이동한 거리를 최신화
    result += dist
    # 먹은거는 바다로 채운다.
    graph[x][y] = 0
    graph[nx][ny] = 0

    x,y = nx,ny
    cnt += 1
    if cnt == shark_size:
        shark_size += 1
        cnt = 0
print(result)
