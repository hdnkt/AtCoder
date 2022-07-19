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


V,E = map(int,input().split())#頂点の数、辺の数
v=[]
for i in range(0,E,1):#[0][1]つなぐところ[2]距離
    v.append(list(map(int,input().split())))
v.sort(key = lambda x:x[2])

print(v)

#初期化
#根なら-size,子なら親の頂点
par = [-1]*V

cost = 0

for i in range(0,E,1):
    if not same(v[i][0],v[i][1]):
        unite(v[i][0],v[i][1])
        cost+=v[i][2]

print(cost)