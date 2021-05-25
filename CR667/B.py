T = int(input())

ret = []
for t in range(T):
    a,b,x,y,n = map(int,input().split())
    
    ans1 = max(a-n,x)*(max(b-max(0,n-a+x),y))
    ans2 = max(b-n,y)*(max(a-max(0,n-b+y),x))
    ret.append(min(ans1,ans2))

for t in range(T):
    print(ret[t])