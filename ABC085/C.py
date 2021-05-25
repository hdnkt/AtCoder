N,Y = map(int,input().split())

ans = [-1,-1,-1]
for i in range(0,N+1,1):
    for j in range(0,N+1-i,1):
        k = N-i-j
        if i*10000 + 5000*j + 1000*k == Y:
            ans = [i,j,k]
            break

print(ans[0],ans[1],ans[2])
