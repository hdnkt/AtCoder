from math import sqrt

N = int(input())

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


print(sep)