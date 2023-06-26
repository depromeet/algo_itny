import sys

input = sys.stdin.readline
from collections import deque


n = 5
board = [
['R','R','R','B','B'],
['G','G','B','B','B'],
['B','B','B','R','R'],
['B','B','R','R','R'],
['R','R','R','R','R']]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
rgb_visited = [[0 for _ in range(n)] for _ in range(n)]
rb_visited = [[0 for _ in range(n)] for _ in range(n)]
rgb_ans = 0
rb_ans = 0


def rgb_dfs(x,y,color):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and rgb_visited[nx][ny] == 0:
            if color == board[nx][ny]:
                rgb_visited[nx][ny] = 1
                rgb_dfs(nx,ny,board[nx][ny])
            

def rb_dfs(x,y,color):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and rb_visited[nx][ny] == 0:
            if color == board[nx][ny] or (color == 'R' and board[nx][ny] == 'G') or ( color == 'G' and board[nx][ny] == 'R'):
                rb_visited[nx][ny] = 1
                rb_dfs(nx,ny,board[nx][ny])



for i in range(n):
    for j in range(n):
        if rgb_visited[i][j] == 0:
            rgb_visited[i][j] = 1
            rgb_dfs(i,j,board[i][j])
            rgb_ans += 1
        
        if rb_visited[i][j] == 0:
            rb_visited[i][j] = 1
            rb_dfs(i,j,board[i][j])
            rb_ans += 1



print(rgb_ans,rb_ans)
