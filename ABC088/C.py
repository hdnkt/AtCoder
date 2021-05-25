c = [list(map(int,input().split())) for i in range(3)]

ans = True
for i in range(3):
        for j in range(3):
            if c[i][j]-c[i][(j+1)%3] != c[(i+1)%3][j]-c[(i+1)%3][(j+1)%3]:
                ans = False
                break

for i in range(3):
        for j in range(3):
            if c[j][i]-c[(j+1)%3][i] != c[j][(i+1)%3]-c[(j+1)%3][(i+1)%3]:
                ans = False
                break

print("Yes" if ans else "No")