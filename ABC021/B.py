N = int(input())
a,b = map(int,input().split())
K = int(input())
P = [a,b]+list(map(int,input().split()))
le = len(P)
P = list(set(P))
if len(P)==le:
    print("YES")
else:
    print("NO")