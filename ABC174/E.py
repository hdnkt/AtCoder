
N,K = map(int,input().split())
A = list(map(int,input().split()))

def isable(n):
    tmp = 0
    for i in range(N):
        tmp += (A[i]-0.5)//n
    if K >= tmp:
        return True
    else:
        return False


left = 0
right = 10**9

while right-left != 1:
    if isable((right+left)//2):
        right=(right+left)//2
    else:
        left=(right+left)//2

print(right)