from collections import deque 
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

N = int(input())
P = [0]+list(map(int,input().split()))#index合わせ
#初期化
#根なら-size,子なら親の頂点
par = [-1]*(N+1)#index合わせ
#スタック
s = deque([])#append pop

for i in range(1,N+1,1):
    if P[i]>0:
        unite(i,P[i])
    else:#要請未定
        if par[i]==-1:#独り
            if len(s)>0:
                unite(s.pop(),i)
            else:
                s.append(i)
count=0
for i in range(1,N+1,1):
    if par[i]<0:#根なら
        count += size(i)-1
    if par[i]==-1:
        count+=1
print(count)

            