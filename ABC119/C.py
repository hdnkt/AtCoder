#bit全探索の亜種(4種全探索)
#itertools.product([0,1,2,3],repeat=N)

import itertools
N,A,B,C = map(int,input().split())
l = [int(input()) for i in range(0,N,1)]

ans = 10**10
for ABCD in itertools.product([0,1,2,3],repeat=N):
    tmp = [[] for i in range(4)]
    for i in range(0,N,1):
        tmp[ABCD[i]].append(l[i])
    score = 0
    owaowari = False
    for i in range(3):#Dはくっ付ける必要なし
        if len(tmp[i])==0:
            owaowari = True
            break
        score+=10*max(len(tmp[i])-1,0)
    if owaowari: continue
    score+=abs(A-sum(tmp[0]))
    score+=abs(B-sum(tmp[1]))
    score+=abs(C-sum(tmp[2]))
    ans = min(ans,score)


print(ans)
