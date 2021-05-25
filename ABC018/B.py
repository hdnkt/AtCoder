S = list(input())
N = int(input())


for i in range(N):
    l,r = map(int,input().split())

    S = S[0:l-1]+list(reversed(S[l-1:r]))+S[r:len(S)]

print("".join(S))
    