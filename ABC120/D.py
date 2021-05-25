#Union Find
#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]

N,M = map(int,input().split())
A=[]
B=[]
for i in range(0,M,1):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
#初期化
#根なら-size,子なら親の頂点
par = [-1]*(N+1)

ans = []
tmpans = N*(N-1)//2
for i in range(M-1,-1,-1):
    ans.append(tmpans)
    if same(A[i],B[i]):
        tmpans = tmpans
    else:
        tmpans -= size(A[i])*size(B[i])
        unite(A[i],B[i])

for i in range(M-1,-1,-1):
    print(ans[i])