N,M = map(int,input().split())
A=[]
for i in range(0,N,1):
    a = list(map(int,input().split()))
    A.append(a[1::])

ans = [i for i in range(1,M+1,1)]
for i in range(0,N,1):
    ans = list(set(ans) & set(A[i]))
print(len(ans))
