N=int(input())
TA=[list(map(int,input().split())) for i in range(N)]

l,r=TA[0]

for i in range(N):
    T,A=TA[i]

    if l%T!=0:
        l1=(l-l%T)+T
    else:
        l1=l
    r1=(l1//T)*A
    
    if r%A!=0:
        r2=(r-r%A)+A
    else:
        r2=r
    l2=(r2//A)*T

    if r1 < r:
        l=l2
        r=r2
    elif l2 < l:
        l=l1
        r=r1
    else:
        l=min(l1,l2)
        r=min(r1,r2)

print(l+r)

