T = int(input())

ret = []
for t in range(T):
    a,b = map(int,input().split())

    ans = abs(a-b)//10
    if abs(a-b)%10!=0:
        ans+=1
    
    ret.append(ans)

for t in range(T):
    print(ret[t])