R,C,K = map(int,input().split())
N = int(input())

RC = {}
Rs = [0]*(R+1)
Cs = [0]*(C+1)

for i in range(N):
    r,c = map(int,input().split())
    Rs[r]+=1
    Cs[c]+=1
    RC[tuple([r,c])]=0
#そのRでとる飴の数がKになるRの数
RK = [0]*(C+1)
for i in range(1,R+1):
    RK[Rs[i]]+=1
ans = 0
for i in range(1,C+1):
    if K-Cs[i] >= 0 and K-Cs[i]<=C:
        ans+=RK[K-Cs[i]]
    
for i,j in RC:
    if Rs[i]+Cs[j]==K:
        ans-=1
    elif Rs[i]+Cs[j]==K+1:
        ans+=1

print(ans)

