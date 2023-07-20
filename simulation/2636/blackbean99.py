from collections import deque
n, m = map(int, input().split())
cheeze = []
cnt = 0
for i in range(n):
    cheeze.append(list(map(int, input().split())))
    cnt += sum(cheeze[i])  # 전체 치즈 갯수 카운트
    
cycle = 1    
    
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs():
    q = deque([(0, 0)])
    melted = deque([])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                # 공기면?
                if cheeze[nx][ny] == 0: 
                    q.append((nx, ny))
                # 치즈면 한 번에 녹여야 한다
                elif cheeze[nx][ny] == 1:
                    melted.append((nx, ny))
    # 치즈 녹이기
    for x, y in melted:
        cheeze[x][y] = 0 
    # 현재 녹인 개수
    return len(melted)  
                    
while True:
    visited = [[0] * m for _ in range(n)]
    meltCnt = bfs()
    cnt -= meltCnt

    if cnt == 0:  # 치즈를 다 녹였으면
        print(cycle, meltCnt, sep='\n')  # 시간과 직전에 녹인 치즈 갯수를 출력
        break
    cycle += 1