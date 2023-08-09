import sys, collections

# 입력부
k = int(sys.stdin.readline())
m , n = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# dx, dy : 일반적인 동서남북 4방향
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# hx, hy : 특수 이동인 8방향
hx = [-1,-2,-1,-2,1,2,1,2]
hy = [-2,-1,2,1,-2,-1,2,1]

# check : 3차원 검사 배열
check = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]

# go : (a,b)에서 시작하여 특수이동, 일반이동을 모두 고려했을 때 도착점으로 가기 위한 최소 동작 횟수를 리턴하는 함수
def go(a,b):
    q = collections.deque()
    q.append((a,b,0,0))
    # 처음에는 특수 이동을 쓰지 않았으므로 [a][b][0]이다
    check[a][b][0] = True
    while q:
        # x, y : 현재 x좌표, y좌표
        # skill : 현재 특수 이동을 한 횟수
        # cnt : 그때의 동작 횟수
        x,y,skill, cnt = q.popleft()
        
        # 도착점이면 동작 횟수 리턴
        if x == n - 1 and y == m - 1:
            return cnt
            
        # 일반적인 4방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny][skill] == False:
                    if table[nx][ny] == 0:
                        check[nx][ny][skill] = True
                        # 특수 이동을 쓰지 않았으므로 skill은 증가시키지 않고 큐에 넣는다
                        q.append((nx, ny, skill, cnt + 1))

        # 특수 이동이 가능한 경우
        if skill < k:
            # 특수 이동 8방향 탐색
            for i in range(8):
                nx, ny = x + hx[i], y + hy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    # 현재 특수 이동을 하게 되면 가려는 정점은
                    # 현재 특수 이동 횟수 + 1번째에 방문하는 것이므로
                    # check[nx][ny][skill]이 아니라
                    # check[nx][ny][skill + 1]을 체크해야 한다
                    if check[nx][ny][skill + 1] == False:
                        if table[nx][ny] == 0:
                            check[nx][ny][skill + 1] = True
                            # 다음 이동을 위해 특수 이동을 한번 썼기 때문에 skill을 1증가 시키고 큐에 넣는다
                            q.append((nx,ny,skill+1,cnt + 1))
    
    # 불가능한 경우 -1 리턴
    return -1

# 정답 출력
print(go(0,0))