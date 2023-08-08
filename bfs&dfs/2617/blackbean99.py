n, m = map(int, input().split())
data = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    data[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if data[i][k] and data[k][j]:
                data[i][j] = 1
                
target_distance = (n) // 2

no_mid = 0
for i in range(1, n+1):
    count_less = 0
    count_greater = 0
    for j in range(1, n+1):
        if i == j:
            continue
        if data[i][j] == 1:
            count_greater += 1
        elif data[j][i] == 1:
            count_less += 1
    if count_less > target_distance or count_greater > target_distance:
        no_mid += 1

print(no_mid)
