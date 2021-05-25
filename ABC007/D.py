a,b = map(int,input().split())

#dp_kakutei[]:Aよりちいさいことが確定していて４も９もでてこない
#dp_hikakutei[]:いまのところAと同じ大きさで４も９もでてこない

A = list(map(int,list(str(b))))
N = len(A)
dp_k=[0 for i in range(N)]
dp_h=[0 for i in range(N)]

if A[0]<5:
    dp_k[0]= A[0]
elif A[0]<10:
    dp_k[0]=A[0]-1
else:
    dp_k[0]=A[0]-2

if A[0]!=4 and A[0]!=9:
    dp_h[0]=1

for i in range(1,N):
    if A[i]<5:
        dp_k[i]=(dp_h[i-1])*(A[i])+dp_k[i-1]*8
    elif A[i]<10:
        dp_k[i]=(dp_h[i-1])*(A[i]-1)+dp_k[i-1]*8
    else:
        dp_k[i]=(dp_h[i-1])*(A[i]-2)+dp_k[i-1]*8

    if A[i]!=4 and A[i]!=9:
        dp_h[i]=dp_h[i-1]

B_forbid = b+1-dp_k[N-1]-dp_h[N-1]

a-=1
A = list(map(int,list(str(a))))
N = len(A)
dp_k=[0 for i in range(N)]
dp_h=[0 for i in range(N)]

if A[0]<5:
    dp_k[0]= A[0]
elif A[0]<10:
    dp_k[0]=A[0]-1
else:
    dp_k[0]=A[0]-2

if A[0]!=4 and A[0]!=9:
    dp_h[0]=1

for i in range(1,N):
    if A[i]<5:
        dp_k[i]=(dp_h[i-1])*(A[i])+dp_k[i-1]*8
    elif A[i]<10:
        dp_k[i]=(dp_h[i-1])*(A[i]-1)+dp_k[i-1]*8
    else:
        dp_k[i]=(dp_h[i-1])*(A[i]-2)+dp_k[i-1]*8

    if A[i]!=4 and A[i]!=9:
        dp_h[i]=dp_h[i-1]

A_forbid = a+1-dp_k[N-1]-dp_h[N-1]

print(B_forbid-A_forbid)