import sys
input = sys.stdin.readline
import copy

n, m, k = map(int, input().split())
fireballs = []
for _ in range(m):
    fireballs.append(list(map(int, input().split())))

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]
ans = 0 

""" 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.

이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
파이어볼은 4개의 파이어볼로 나누어진다.
나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
질량이 0인 파이어볼은 소멸되어 없어진다. """

for _ in range(k):
    fireballs_board = [[[] for _ in range(n+1)] for _ in range(n+1)]
    next_fireballs = []
    """ 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
    이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다. """
    """ print('fireballs',fireballs) """
    for r,c,m,s,d in fireballs:
        nr = (r + dr[d] * s) % n
        nc = (c + dc[d] * s) % n
        fireballs_board[nr][nc].append([m,s,d])
    
    """ 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다. """
    for i in range(n):
        for j in range(n):
            if len(fireballs_board[i][j]) == 0:
                continue
            if len(fireballs_board[i][j]) >= 2:
                acc_m = 0
                acc_s = 0
                even_count = 0
                odd_count = 0
                for [m,s,d] in fireballs_board[i][j]:
                    acc_m += m
                    acc_s += s
                    if d % 2 == 0:
                        even_count += 1
                    else:
                        odd_count += 1
                nm = acc_m//5
                ns = acc_s//len(fireballs_board[i][j])
                if even_count > 0 and odd_count > 0:
                    nd = [1,3,5,7]
                else:
                    nd = [0,2,4,6]
                
                """ 파이어볼은 4개의 파이어볼로 나누어진다.
                나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
                질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
                속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
                합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
                질량이 0인 파이어볼은 소멸되어 없어진다. """
                if nm > 0:
                    for d in nd:
                        next_fireballs.append(([i,j,nm,ns,d]))
            else:
                nm,ns,nd = fireballs_board[i][j][0]
                next_fireballs.append([i,j,nm,ns,nd])
    

    fireballs = copy.deepcopy(next_fireballs)

# print('fireballs',fireballs)
for _,_,m,_,_ in fireballs:
    ans += m
print(ans)




