H,W = map(int,input().split())
S = [list(input()) for i in range(H)]

ans = 0

for i in range(H):
    for j in range(0,W-1):
        if S[i][j]=="." and S[i][j+1]==".":
            ans += 1

for j in range(W):
    for i in range(0,H-1):
        if S[i][j]=="." and S[i+1][j]==".":
            ans+=1

print(ans)