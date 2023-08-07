N, L = map(int, input().split())
map_arr = [list(map(int, input().split())) for _ in range(N)]

SAME = 0
UP = 1
DOWN = -1


def can_go(L, arr):
    visited = [False] * len(arr)
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff == SAME:
            continue
        elif diff == UP:  # 올라가는 경우
            cur_point = i-1
            for j in range(cur_point, cur_point-L, -1):  # 역으로 가야함
                if j < 0 or arr[j] != arr[i-1] or visited[j]:
                    return False
                else:
                    visited[j] = True
        elif diff == DOWN:  # 내려가는 경우
            for j in range(i, i+L):  # 순방향
                if j >= len(arr) or arr[j] != arr[i] or visited[j]:
                    return False
                else:
                    visited[j] = True
        else:
            return False
    return True


def solution(N, L, map_arr):
    result = 0
    checking_list = map_arr + [[map_arr[j][i]
                                for j in range(N)] for i in range(N)]
    for c in checking_list:
        if len(list(set(c))) == 1:
            result += 1
        else:
            if can_go(L, c):
                result += 1
    return result


print(solution(N, L, map_arr))
