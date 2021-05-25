N = int(input())

S = sum(list(map(int,list(str(N)))))

print("Yes" if N%S ==0 else "No")