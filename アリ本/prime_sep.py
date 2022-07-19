from math import sqrt

def prime_sep(N):
    #素因数分解
    sep = []
    for i in range(2,int(sqrt(N))+2,1):
        if N % i ==0:
            count = 0
            while N % i == 0:
                N = N//i
                count += 1
            sep.append([i,count])
    if N != 1:
        sep.append([N,1])
    return sep

ans = 0
for i in range(20):
    a = list(map(int,input().split()))
    for j in range(len(a)):
        tmp = prime_sep(a[j])
        if len(tmp)==1 and tmp[0][1]==1:
            ans+=1

print(ans)
