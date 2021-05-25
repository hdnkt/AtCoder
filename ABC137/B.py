K,X = map(int,input().split())

S = []
for i in range(X-K+1,X+K,1):
    S.append(i)
print(" ".join(map(str,S)))