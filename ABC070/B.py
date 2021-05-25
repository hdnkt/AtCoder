A,B,C,D = map(int,input().split())

s = max(A,C)
e = min(B,D)

print(e-s if e-s>0 else 0)