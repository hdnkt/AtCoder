N = int(input())
A = list(map(int,input().split()))
sum1 = 0
for i in range(0,N,1):
    sum1 += 1/A[i]
print(1/sum1)