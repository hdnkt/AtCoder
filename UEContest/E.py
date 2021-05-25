import itertools

S,N = map(int,input().split())
origin = list(map(int,list(str(S))))
S = len(str(S))

ans = 12

flag = False
for it in itertools.product([6,9],repeat=S):
    tmp = 0
    for i in range(S):
        tmp+=it[i]*(10**(S-i-1))
    
    count = 0
    for i in range(S):
        if origin[i]!=it[i]:
            count+=1

    if tmp%N==0:
        ans = min(count,ans)


print(-1 if ans == 12 else ans)