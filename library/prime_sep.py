#Nを素因数分解して[[素数、使う個数],[素数、使う個数],...]
#のリストで返す
from math import sqrt
def prime_sep(N):
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



N = int(input())
print(prime_sep(N))