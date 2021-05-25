N = int(input())
A  = list(map(int,input().split()))

maxA = max(A)
era = [0]*(maxA+1)

for i in range(0,N,1):
    if era[A[i]]==0:#脱落
        era[A[i]]=1#除＋カウント
    else:
        era[A[i]]=-1#除には参加カウントしない

ans = 0

for i in range(1,maxA+1,1):
    if era[i]==1:
        for j in range(2*i,maxA+1,i):
            era[j]=0
        ans+=1
    elif era[i]==-1:
        for j in range(2*i,maxA+1,i):
            era[j]=0

print(ans)
            

