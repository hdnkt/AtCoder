import itertools

s = input()

ans = 0
for i in itertools.product([0,1],repeat=len(s)-1):
    tmpans = 0
    tmp = [0]
    for j in range(len(i)):
        if i[j]==1:
            tmp.append(j+1)

    tmp.append(len(s))
    
    for j in range(len(tmp)-1):
        tmpans+=int(s[tmp[j]:tmp[j+1]])
    
    ans+=tmpans

print(ans)