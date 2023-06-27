import sys
sys.setrecursionlimit(100000)

def input_grid():
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    return N, arr

def print_result(result1, result2):
    print(F"{result1} {result2}");


def solution(N, arr):
    if not arr:
        return 0, 0
    arr2 = [arr[i][:] for i in range(N)]
    normal_cnt = get_normal_count(arr)
    strange_cnt = get_strange_count(arr2)
    return normal_cnt, strange_cnt


def get_normal_count(arr):
    normal_value_list = ['R','G','B']
    count=0;
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            for k in normal_value_list:
                if arr[i][j] == k:
                    count += 1
                    visited_check(arr, i, j, k)
    return count



def get_strange_count(arr):
    normal_value_list = ['R','B']
    count=0;
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'G':
                arr[i][j] = 'R'
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            for k in normal_value_list:
                if arr[i][j] == k:
                    count += 1
                    visited_check(arr, i, j, k)
                    break
    return count


def visited_check(arr, i, j, value):
    x_len = len(arr)
    y_len = len(arr[0])
    if i < 0 or j<0 or i>=x_len or j>=y_len or arr[i][j] != value:
        return
    arr[i][j] = 'N'

    visited_check(arr, i-1, j, value);
    visited_check(arr, i+1, j, value);
    visited_check(arr, i, j-1, value);
    visited_check(arr, i, j+1, value);



if __name__ == '__main__':
    N, arr = input_grid()
    result1, result2 = solution(N, arr)
    print_result(result1,result2)