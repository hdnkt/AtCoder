N=int(input())
t=[0]
x=[0]
y=[0]
for i in range(0,N,1):
    tmpT,tmpX,tmpY = map(int,input().split(sep=" "))
    t.append(tmpT)
    x.append(tmpX)
    y.append(tmpY)

#最速で到達した時の残り時間が偶数なら到達可能
for i in range(1,N+1,1):
    if abs(x[i]-x[i-1])+abs(y[i]-y[i-1]) > t[i]-t[i-1]:
        print("No")
        exit()
    if (t[i]-t[i-1]-(abs(x[i]-x[i-1])+abs(y[i]-y[i-1])))%2==1:
        print("No")
        exit()
print("Yes")