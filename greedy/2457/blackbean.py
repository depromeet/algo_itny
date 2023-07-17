from collections import deque

n = int(input())
data = []
for i in range(n):
    s_month, s_day, e_month, e_day = map(int,input().split())    
    data.append((s_month*100 + s_day, e_month * 100+ e_day))

data.sort(key = lambda x:(x[0],x[1]))

#선택한 꽃의 개수
cnt = 0

end = 0
target = 301
while data:
    # 마지막 꽃의 지는 날이 제일 빨리 피는 꽃보다 작으면 
    if target >= 1201 or target < data[0][0]:
        break
    for _ in range(len(data)):
        if target >= data[0][0]:
            if end <= data[0][1]:
                end = data[0][1]
            data.remove(data[0])
        else:
            break
    target = end
    cnt += 1

if target < 1201:
    print(0)
else:
    print(cnt)