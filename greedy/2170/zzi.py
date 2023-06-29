import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
ans = 0
arr.sort(key=lambda x:(x[0],x[1]))

start = -1000000001
end = -1000000001
acc = 0
for x,y in arr:
    # 처음
    if start == -1000000001 and end == -1000000001:
        start = x
        end = y
    # 이후
    else:
        if x <= end:
            end = max(y,end)
        else:
            ans += abs(end - start)
            start = x
            end = y

ans += abs(end - start)

print(ans)
