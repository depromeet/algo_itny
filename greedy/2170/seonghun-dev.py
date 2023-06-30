import sys
input = sys.stdin.readline


def input_value():
    N = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(N)]
    return lines


def solution(lines):
    lines.sort()
    start = lines[0][0]
    end = lines[0][1]
    length = 0
    if len(lines) == 1:
        return end-start
    for line in lines[1:]:
        if line[0] <= end:
            if line[1] > end:
                end = line[1]
        else:
            length += end-start
            start = line[0]
            end = line[1]
    length += end - start
    return length


def old_solution(lines):
    # (x, y) : 1
    dir_vector = {}
    if len(lines) == 1:
        return 0
    prev_value = (None, None)
    for i, v in enumerate(lines):
        if prev_value == (None, None):
            prev_value = (v[0], v[1])
        else:
            x_vec = v[0] - prev_value[0]
            y_vec = v[1] - prev_value[1]
            prev_value = (v[0], v[1])
            print(x_vec)
            print(y_vec)
            vec_size = (x_vec ** 2 + y_vec ** 2) ** 0.5
            x_dir_vec = x_vec / vec_size
            y_dir_vec = y_vec / vec_size
            if dir_vector.get((x_dir_vec, y_dir_vec)) is None:
                dir_vector[(x_dir_vec, y_dir_vec)] = vec_size
            else:
                dir_vector[(x_dir_vec, y_dir_vec)] = max(
                    dir_vector[(x_dir_vec, y_dir_vec)], vec_size)
    return True


if __name__ == '__main__':
    lines = input_value()
    print(solution(lines))
