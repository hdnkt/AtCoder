T = int(input())

ret = []
for t in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    ans = [0 if l[i]==0 else a[i] for i in range(n)]


    plus = []
    minus = []
    for i in range(n):
        if l[i]==0:
            if a[i]>=0:
                plus.append(a[i])
            else:
                minus.append(a[i])
    minall = sum(minus)
    
    bp = n

    plus.sort(reverse=True)
    ruiseki = 0
    for i in range(n):
        if l[i]==1:
            ruiseki+=a[i]
        else:
            if len(plus)>0 and plus[len(plus)-1]+ruiseki+minall<0:
                ans[i]=plus.pop()
            else:
                bp = i
                break
    
    for i in range(bp,n):
        if l[i]==0:
            if len(minus)>0:
                ans[i]=minus.pop()
            else:
                ans[i]=plus.pop()
    
    ret.append(ans)

for t in range(T):
    print(" ".join(list(map(str,ret[t]))))




