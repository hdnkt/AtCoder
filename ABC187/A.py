A,B = input().split()

A = sum(list(map(int,list(A))))
B = sum(list(map(int,list(B))))


print(max(A,B))