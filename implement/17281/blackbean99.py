#백준 17281번 야구공
from itertools import permutations

N=int(input())
result=[list(map(int,input().split())) for _ in range(N)]

c=[1,2,3,4,5,6,7,8]
c_m=permutations(c,8)
answer=0


for ball in c_m:
    score=0
    #선수들 순서를 구함
    case=list(ball)
    case.insert(3,0)
    print(case)
    print("-------------")
    inning=0
    out=0
    player=0
    
    base=[0,0,0]
    while inning<N:
        n_p=case[player]
        now=result[inning][n_p]

        #아웃
        if now==0:
            out+=1
        #안타
        elif now==1:
            if base[2]==1:
                score+=1
                base[2]=0
            if base[1]==1:
                base[1]=0
                base[2]=1
            if base[0]==1:
                base[0]=0
                base[1]=1
            base[0]=1
        #2루타
        elif now==2:
            if base[2]==1:
                score+=1
                base[2]=0
            if base[1]==1:
                base[1]=0
                score+=1
            if base[0]==1:
                base[0]=0
                base[2]=1
            base[1]=1
        #3루타
        elif now==3:
            if base[2]==1:
                score+=1
                base[2]=0
            if base[1]==1:
                base[1]=0
                score+=1
            if base[0]==1:
                base[0]=0
                score+=1
            base[2]=1
        #홈런
        elif now==4:
            if base[2]==1:
                score+=1
                base[2]=0
            if base[1]==1:
                base[1]=0
                score+=1
            if base[0]==1:
                base[0]=0
                score+=1
            score+=1

        player=(player+1)%9

        if out==3:
            inning+=1
            base=[0,0,0]
            out=0


    answer=max(answer,score)

print(answer)