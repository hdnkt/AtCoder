H,N = map(int,input().split())
A = list(map(int,input().split()))#SUM使え

for i in range(0,N,1):
    H -= A[i]
    if H <= 0:
        print("Yes")
        exit()

print("No")