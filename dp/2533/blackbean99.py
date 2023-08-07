# 2 - 1,000,000
n = int(input())
graphs = [[] for _ in range(n+1)]

socialized = [0] * (n+1)

for i in range(n-1):
    start, end = map(int,input().split())
    graphs[start].append(end)
    

graphs.sort(key=len, reverse=True)

def is_socialized(socialized):
    for i in socialized:
        if i == 0:
            return False
    return True

already = 0

for graph in graphs:    
    for index in graph:
        print("index : ", index)
#       자식이 없을 경우에 socialized
        if len(graphs[index]) == 0:
            already += 1
            socialized[index] = 1
        else:
            flag = False
            #         자식이 있는데 0이면 넘어가기
            for sub in graphs[index-1]:
                print(index , " : ", sub)
                if socialized[sub] == 0:
                    flag = False
                    break
                else:
                    flag = True
            #         index 의 자식이 전부 1이면 socialized
            if flag:
                already += 1
                socialized[index] = 1
        if is_socialized(socialized):
            break
    if is_socialized(socialized):
        break
    print(already)


# 1 : 2, 3, 4
# 2 : 5, 6
# 4 : 7, 8

# 1 체크하고 아니면
# 2 체크하고 아니면
# 4 체크한다. 끝
# 4체크하고 
# dp...
# 1. 가장 친구가 많은 순으로 체크해보자
# 4 : 7,8,9
# 1 : 2, 3
# 3 : 5, 6
# 2 : 4
# 3개

# 4 체크 하고. 아니면
# 1체크하고 아니면
# 3 체크하면 끝