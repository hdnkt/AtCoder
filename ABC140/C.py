N = int(input())
B = list(map(int,input().split()))+[100000000000]
A=[B[0]]
for i in range(1,N,1):
    A.append(min(B[i],B[i-1]))
print(sum(A))