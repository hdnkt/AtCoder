INF = 10**10

R,C,K = map(int,input().split())
s = [list(input()) for i in range(R)]

num = [[INF if s[i][j]=="o" else 0 for j in range(C)]for i in range(R)]

for i in range(R):
    tmpdist=INF
    for j in range(C):
        if s[i][j]=="x":
            tmpdist=0
        num[i][j]=min(tmpdist,num[i][j])
        tmpdist+=1
    tmpdist=INF
    for j in range(C-1,-1,-1):
        if s[i][j]=="x":
            tmpdist=0
        num[i][j]=min(tmpdist,num[i][j])
        tmpdist+=1

for j in range(C):
    tmpdist=INF
    for i in range(R):
        if num[i][j]<tmpdist:
            tmpdist=num[i][j]
        num[i][j]=min(tmpdist,num[i][j])
        tmpdist+=1
    tmpdist=INF
    for i in range(R-1,-1,-1):
        if num[i][j]<tmpdist:
            tmpdist=num[i][j]
        num[i][j]=min(tmpdist,num[i][j])
        tmpdist+=1


ans = 0
for i in range(K-1,R-K+1):
    for j in range(K-1,C-K+1):
        if num[i][j]>=K:
            ans+=1
    
print(ans)