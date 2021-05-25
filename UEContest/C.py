N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))


print("Yes" if sum(A)<=sum(B) else "No")