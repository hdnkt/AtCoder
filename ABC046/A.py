a,b,c = map(int,input().split())

ans = [0]*(101)
ans[a]=1
ans[b]=1
ans[c]=1
print(sum(ans))