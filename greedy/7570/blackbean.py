n = int(input())
data = list(map(int, input().split()))

idx = [-1] * (n+1)
for i, v in enumerate(data):
    idx[v] = i # 각 수가 어디있는지 기록

longest = 0
cnt = 1
for num in range(1, n):
    if idx[num] < idx[num + 1]:
        cnt += 1
    else:
        # 최장 오름차순 배열 길이 갱신
        longest = max(longest, cnt)
        cnt = 1
print( n - longest if n != 1 else 0)