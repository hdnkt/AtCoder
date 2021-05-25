H,W = map(int,input().split())
N = int(input())
a = list(map(int,input().split()))

ans = [[0 for i in range(W)] for j in range(H)]

def nex(x,y):
    if y%2 == 0 and x == H-1:
        return x,y+1
    elif y%2 == 1 and x==0:
        return x,y+1
    elif y%2 ==0:
        return x+1,y
    else:
        return x-1,y

nowX,nowY = 0,0
for i in range(N):
    for j in range(a[i]):
        ans[nowX][nowY] = i+1
        nowX,nowY = nex(nowX,nowY)

for i in range(len(ans)):
    print(" ".join(list(map(str,ans[i]))))