import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
ans = 0
cnt = 0



def check_air_or_hole():
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] == -1:
                board[i][j] = 0

    def get_zero_list(i,j):
        for k in range(4):
            ni = dx[k] + i
            nj = dy[k] + j
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and board[ni][nj] == 0:
                visited[ni][nj] = 1
                zero_list.append([ni,nj])
                get_zero_list(ni,nj)

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and board[i][j] == 0:
                zero_list = []
                get_zero_list(i,j)
                is_air = False
                for x,y in zero_list:
                    if x == 0 or y == 0 or x == n-1 or y == m-1:
                        is_air = True
                if not is_air:
                    for x,y in zero_list:
                        board[x][y] = -1

# 다 녹았는지 확인
def all_melt_check():
    is_all_melt = True
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                is_all_melt = False
                count += 1
    return is_all_melt,count

while True:
    check_air_or_hole()
    melt = []
    is_all_melt,count = all_melt_check()
    if is_all_melt:
        break
    ans += 1
    if count > 0:
        cnt = count
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                is_melt = False
                for k in range(4):
                    ni = dx[k] + i
                    nj = dy[k] + j
                    if 0 <= ni < n and 0 <= nj < m and board[ni][nj] != 0:
                        continue
                    else:
                        is_melt = True
                        break
                if is_melt:
                    melt.append([i,j])
    
    for x,y in melt:
        board[x][y] = 0

print(ans)
print(cnt)

