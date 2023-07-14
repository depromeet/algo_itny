import sys
from collections import deque

input = sys.stdin.readline

board = [list(input().rstrip()) for _ in range(12)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
pop_list = []
ans = 0

def pop_check(color,count,x,y,list):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 12 and 0 <= ny < 6 and board[nx][ny] == color and visited[nx][ny] == 0 and board[nx][ny] != '.':
            list.append((nx,ny))
            visited[nx][ny] = 1
            pop_check(color,count+1,nx,ny,list)
    return list

def pop():
    global ans 
    ans += 1
    for x,y in pop_list:
        board[x][y] = '.'

def gravity():
    for i in range(6):
        list = []
        for j in range(11,-1,-1):
            if board[j][i] != '.':
                list.append(board[j][i])
                board[j][i] = '.'
        for k in range(len(list)):
            board[11-k][i] = list[k]


while True:
    pop_list = []
    for i in range(12):
        for j in range(6):
            visited = [[0 for _ in range(6)] for _ in range(12)]
            visited[i][j] = 1
            list = pop_check(board[i][j],1,i,j,[(i,j)])
            if len(list) >= 4:
                for l in list:
                    if l not in pop_list:
                        pop_list.append(l)
    if len(pop_list) == 0:
        break
    else:
        pop()
        gravity()

print(ans)
