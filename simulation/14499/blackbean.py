from collections import deque

n,m,x,y,k = map(int,input().split())

graph = []
# [y][x]
for i in range(n):
    graph.append(list(map(int,input().split())))

# k개 만큼의 명령
q = deque()
order = list(map(int,input().split()))
for i in range(k):
    q.append(order[i])

# 위,아래,  북, 동, 서, 남,
# dice = [1,6,2,3,4,5]
dice = [0,0,0,0,0,0]
def rotate(dice, dir):
    new_dice = [0,0,0,0,0,0]
    # 동쪽
    if dir == 1:
        # 위 <= 서
        new_dice[0] = dice[3]
        # 동 <= 위
        new_dice[3] = dice[0]
        # 서 <= 아래
        new_dice[4] = dice[1]
        # 아래 <= 동
        new_dice[1] = dice[3]
        new_dice[2] = dice[2]
        new_dice[5] = dice[5]
        # 서쪽
    elif dir == 2:
        new_dice[0] = dice[3]
        new_dice[4] = dice[0]
        new_dice[3] = dice[1]
        new_dice[1] = dice[4]
        new_dice[2] = dice[2]
        new_dice[5] = dice[5]
        # 북쪽
    elif dir ==3:
        # 북 <= 위
        new_dice[2] = dice[0]
        # 위 <= 남
        new_dice[0] = dice[5]
        # 남 < = 아래
        new_dice[5] = dice[1]
        # 아래 < 북
        new_dice[1] = dice[2]
        # 동
        new_dice[3] = dice[3]
        # 서
        new_dice[4] = dice[4]
    #     남쪽으로 굴리기
    elif dir == 4:
        # 북 <= 아래
        new_dice[2] = dice[1]
        # 위 <= 북
        new_dice[0] = dice[2]
        # 남 <= 위
        new_dice[5] = dice[0]
        # 아래 <= 남
        new_dice[1] = dice[5]
        # 동
        new_dice[3] = dice[3]
        # 서
        new_dice[4] = dice[4]
    return new_dice

answer = []
# 동쪽은1,
# 서쪽은2,
# 북쪽은3,
# 남쪽은4
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

while q:
    dir = q.popleft()
    # 0,0 ->
    nx = x + dx[dir - 1]
    ny = y + dy[dir - 1]
    new_dice = rotate(dice, dir)
    if 0 <= nx < m and 0 <= ny < n:
        # 0이면
        if graph[ny][nx] == 0:
            # 주사위 아랫면을 복사
            graph[ny][nx] = new_dice[1]
            # 윗면을 정답에 추가
            answer.append(new_dice[0])
            dice = new_dice
        # 아니면
        else:
            new_dice[1] = graph[ny][nx]
            graph[ny][nx] = 0
            answer.append(new_dice[0])
            dice = new_dice
        x = nx
        y = ny
for i in answer:
    print(i)
