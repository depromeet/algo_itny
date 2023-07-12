import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = []
r,c,d = map(int,input().split())

for _ in range(n):
    board.append(list(map(int,input().split())))


count = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def is_four_clean(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            return True
    return False

def clean(x,y):
    global count
    if board[x][y] == 0:
        board[x][y] = -1
        count += 1

while True:
    clean(r,c)
    if is_four_clean(r,c):
        d = (d+3)%4
        nx = r + dx[d]
        ny = c + dy[d]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            r = nx
            c = ny
    else:
        nx = r - dx[d]
        ny = c - dy[d]
        if 0 <= nx < n and 0 <= ny < m and not board[nx][ny] == 1:
            r = nx
            c = ny
        else:
            break
    
print(count)


