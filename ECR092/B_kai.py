T = int(input())

ret = []
for t in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    ans = [0 if l[i]==0 else a[i] for i in range(n)]

    ireru = []
    for i in range(n):
        if l[i]==0:
            ireru.append(a[i])
    ireru.sort()

    for i in range(n):
        if l[i]==0:
            ans[i]=ireru.pop()
    
    ret.append(ans)

for t in range(T):
    print(" ".join(list(map(str,ret[t]))))