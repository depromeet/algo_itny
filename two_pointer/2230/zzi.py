import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [0] * n
for i in range(n):
    numbers[i] = int(input().rstrip())

numbers.sort()
ans = numbers[n-1]-numbers[0]
lt = 0
rt = 1

while rt < n and lt <= rt:
    diff = numbers[rt]-numbers[lt]
    if diff == m:
        ans = m
        break
    if diff > m:
        ans = min(ans,diff)
        lt += 1
    if diff < m:
        rt += 1

print(ans)
