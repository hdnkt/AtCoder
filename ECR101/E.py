T = int(input())

ans = []

for t in range(T):
    n,k = map(int,input().split())
    s = list(input())
    for i in range(n):
        if s[i]=="0":
            s[i]="1"
        else:
            s[i]="0"
    count1 = 0
    if k > 20:
        count1 = s[0:k-20].count("1")
    s = "".join(s)

    dic = {}
    for i in range(n-k+1):
        if k <= 20:
            dic[int(s[i:i+k],2)]=0
        else:
            if count1==0:
                dic[int(s[i+k-20:i+k],2)]=0
            count1 -= int(s[i])
            count1 += int(s[i+k-20])
        

    tmpans=10**10
    for i in range(0,n+1):
        if not(i in dic):
            tmpans=i
            break
    if tmpans < pow(2,k):
        ans.append("YES")
        ans.append(format(tmpans,"0"+str(k)+"b"))
    else:
        ans.append("NO")

for i in range(len(ans)):
    print(ans[i])