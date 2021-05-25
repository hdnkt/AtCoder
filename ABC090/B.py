A,B = map(int,input().split())

ans = 0
for i in range(A,B+1,1):
    tmp = list(str(i))
    is_kai = True
    for j in range(0,len(tmp),1):
        if tmp[j]!=tmp[len(tmp)-1-j]:
            is_kai=False
            break
    if is_kai:
        ans+=1

print(ans)