n, l = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

visited = [[0] * n for _ in range(n)]


def is_possible(row, column, direction):
    temp = []
    if direction == 0:
        for i in range(n - 1):
            if i + l >= n:
                continue
            diff = data[row][i + l] - data[row][i]
            if abs(diff) > 1:
                return False
            # 경사가 1이면
            if diff == 1:
                for j in range(i - l + 1, i + 1):
                    if j < 0 or j + l > n:
                        return False
                    temp.append((row, j))
            # 반대 방향 고려
            elif diff == -1:
                for j in range(i + 1, i + l + 1):
                    if j + l > n:
                        return False
                    temp.append((row, j))
    else:
        for i in range(n - 1):
            diff = data[i + 1][column] - data[i][column]
            if abs(diff) > 1:
                return False
            if diff == 1:
                for j in range(i - l + 1, i + 1):
                    if j < 0 or j + l > n:
                        return False
                    temp.append((j, column))
            elif diff == -1:
                
                for j in range(i + 1, i + l + 1):
                    if j + l > n:
                        return False
                    temp.append((j, column))

    for t in temp:
        if visited[t[0]][t[1]]:
            return False

    for t in temp:
        visited[t[0]][t[1]] = 1

    return True


count = 0
for i in range(n):
    if is_possible(i, 0, 0):
        print(i," : ",0)
        count += 1

for j in range(n):
    if is_possible(0, j, 1):
        print(0," : ",i)
        count += 1
print(count)
