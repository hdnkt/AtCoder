N = int(input())
d = list(map(int,input().split()))

druiseki = [0 for i in range(N)]

for i in range(N):
    for j in range(0,7):
        if i-j >= 0:
            druiseki[i-j]+=d[i]


ans = 0
tmp = 0
for i in range(N-6):
    if druiseki[i]<=5:
        if tmp ==0:
            tmp += 7
        else:
            tmp+=1
    else:
        tmp=0
    ans = max(ans,tmp)

print(ans)

