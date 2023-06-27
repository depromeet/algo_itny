from collections import deque


def input_grid():
    M, N, H = map(int, input().split())
    arr = [[list(map(int, input().split())) for _ in range(N)]
           for _ in range(H)]
    return M, N, H, arr


def solution(M, N, H, arr):
    answer = 0
    queue = deque([])
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 1:
                    queue.append((i, j, k))

    bfs_search(M, N, H, queue)

    if check_exist_zero(M, N, H, arr):
        return -1
    answer = get_max(M, N, H, arr) - 1
    return answer


def bfs_search(M, N, H, queue):
    delta = [(1, 0, 0), (-1, 0, 0), (0, 1, 0),
             (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    while queue:
        z, x, y = queue.popleft()

        for v in delta:
            new_z = z + v[0]
            new_x = x + v[1]
            new_y = y + v[2]
            if 0 <= new_z < H and 0 <= new_x < N and 0 <= new_y < M:
                if arr[new_z][new_x][new_y] == 0:
                    arr[new_z][new_x][new_y] = arr[z][x][y] + 1
                    queue.append((new_z, new_x, new_y))


def check_exist_zero(M, N, H, arr):
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 0:
                    return True
    return False


def get_max(M, N, H, arr):
    max_val = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                max_val = max(max_val, arr[i][j][k])
    return max_val


if __name__ == '__main__':
    M, N, H, arr = input_grid()
    print(solution(M, N, H, arr))
