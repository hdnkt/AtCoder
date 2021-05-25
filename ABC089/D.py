H,W,D = map(int,input().split())

one_to_HW = [[0,0] for i in range(0,H*W+1,1)]

for i in range(1,H+1,1):
    A = [0]+list(map(int,input().split()))
    for j in range(1,W+1,1):
        one_to_HW[A[j]] = [i,j]
    
path = [0]*(H*W+1)

for i in range(D,H*W+1,1):#一つ前からたどり着くのに魔力
    path[i]=abs(one_to_HW[i][0]-one_to_HW[i-D][0])+abs(one_to_HW[i][1]-one_to_HW[i-D][1])

for i in range(D,H*W+1,1):#累積
    path[i]=path[i]+path[i-D]

ans = []
Q = int(input())
for i in range(Q):
    l,r = map(int,input().split())
    ans.append(path[r]-path[l])

for i in range(Q):
    print(ans[i])

