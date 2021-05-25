T = int(input())

ret = []
for t in range(T):
    x,y,k = map(int,input().split())
    ans = (k*y+k-1)//(x-1) +k
    if (k*y+k-1)%(x-1) != 0:
        ans+=1
    ret.append(ans)
for t in range(T):
    print(ret[t])