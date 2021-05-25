
N,T = map(int,input().split())
A = list(map(int,input().split()))

#とりあえず現状の最大値をGET
ans = 0
tmpmin=A[0]
for i in range(len(A)):
    tmpmin=min(A[i],tmpmin)
    ans = max(ans,A[i]-tmpmin)

ret = 0
tmpmin=A[0]
for i in range(len(A)):
    tmpmin=min(A[i],tmpmin)
    if A[i]-tmpmin == ans:
        ret+=1

print(ret)
