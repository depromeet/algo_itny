import sys

input = sys.stdin.readline

n,l = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def right(i):
    visited = [0] * n
    for j in range(1,n):
        diff = board[i][j] - board[i][j-1]
        if abs(diff) > 1:
            return False
        
        # 기울기가 같을 때
        if diff == 0:
            continue

        # 내려가는 경사
        if diff == -1:
            for k in range(j,j+l):
                if k >= n or board[i][j] != board[i][k] or visited[k]:
                    return False
                else:
                    visited[k] = 1
                
        # 올라가는 경사 
        if diff == 1:
            for k in range(j-1,j-l-1,-1):
                if k < 0 or board[i][j-1] != board[i][k] or visited[k]:
                    return False
                else:
                    visited[k] = 1
    return True


def down(i):
    visited = [0] * n
    for j in range(1,n):
        diff = board[j][i] - board[j-1][i]
        if abs(diff) > 1:
            return False
        
        # 기울기가 같을 때
        if diff == 0:
            continue

        # 내려가는 경사
        if diff == -1:
            for k in range(j,j+l):
                if k >= n or board[j][i] != board[k][i] or visited[k]:
                    return False
                else:
                    visited[k] = 1
                
        # 올라가는 경사 
        if diff == 1:
            for k in range(j-1,j-l-1,-1):
                if k < 0 or board[j-1][i] != board[k][i] or visited[k]:
                    return False
                else:
                    visited[k] = 1
    return True



for i in range(n):
    if right(i):
        ans += 1
    if down(i):
        ans += 1 

print(ans)
