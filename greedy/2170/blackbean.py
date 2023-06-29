import sys

length = 0
past_value = 0
max_b = 0
input = sys.stdin.readline
n = int(input())

graph = []

for _ in range(n):
    graph.append(tuple(map(int, input().split())))

graph.sort()

start = graph[0][0]
end = graph[0][1]

for i in range(1,n):
    if graph[i][0] <= end < graph[i][1]:
        end = max(end, graph[i][1])
    # 떨어져서 시작되는 점일 때,
    elif graph[i][0] > end:
        # 기존에 계산했던 점을 누적 계산하고
        length += end - start
        # 새로운 시작점과 끝점을 갱신한다.
        start = graph[i][0]
        end = graph[i][1]

length += end - start
print(length)
