import sys
input = sys.stdin.readline

gears = []
for _ in range(4):
    gears.append(list(input().rstrip()))
k = int(input())
r = [list(map(int, input().split())) for _ in range(k)]

ans = 0

def rotate_clockwise(i):
    gears[i] = [gears[i][-1]] + gears[i][:-1]

def rotate_counterclockwise(i):
    gears[i] = gears[i][1:] + [gears[i][0]]

def check(index,clockwise,counterclockwise,dir):
    global gears

    if index - 1 >= 0:
        if gears[index][6] != gears[index-1][2] and not (index-1) in clockwise and not (index-1) in counterclockwise:
            if dir == 1:
                counterclockwise.append(index-1)
                check(index-1,clockwise,counterclockwise,-1)
            if dir == -1:
                clockwise.append(index-1)
                check(index-1,clockwise,counterclockwise,1)
    if index + 1 <= 3:
        if gears[index+1][6] != gears[index][2] and not (index+1) in clockwise and not (index+1) in counterclockwise:
            if dir == 1:
                counterclockwise.append(index+1)
                check(index+1,clockwise,counterclockwise,-1)
            if dir == -1:
                clockwise.append(index+1)
                check(index+1,clockwise,counterclockwise,1)


for [index, dir] in r:
    clockwise = []
    counterclockwise = []
    if dir == 1:
        clockwise.append(index-1)
    if dir == -1:
        counterclockwise.append(index-1)
    check(index-1,clockwise,counterclockwise,dir)
    for c in clockwise:
        rotate_clockwise(c)
    for c in counterclockwise:
        rotate_counterclockwise(c)

        
for i in range(4):
    if gears[i][0] == '0':
        ans += 0
    else:
        ans += 2**i

print(ans)
