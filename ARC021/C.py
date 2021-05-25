import sys
sys.setrecursionlimit(10**5)


N = int(input())
AB = [list(map(int,input().split())) for i in range(N-1)]

nodes = [[] for i in range(N)]
for i in range(N-1):
    A,B = AB[i]
    A-=1
    B-=1
    nodes[A].append(B)
    nodes[B].append(A)

ansd=0
ans=[]
def func(n,pair):
    if pair!=-1 and len(nodes[n])==1:
        return 1,n
    lis = [[0,n]]
    for i in nodes[n]:
        if i==pair:
            continue
        depth,depthman = func(i,n)
        lis.append([depth,depthman])
    lis.sort(reverse=True)
    if ansd < lis[0][0]+lis[1][0]:
        ans.append([lis[0][1],lis[1][1]])
    depth,depthman = lis[0]
    return depth+1,depthman
func(0,-1)

print(ans[len(ans)-1][0]+1,ans[len(ans)-1][1]+1)
