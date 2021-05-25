#左右それぞれで一番近い神社
#その神社それぞれの左右それぞれで一番近い寺
#はい２ぶたん

INF = 10**12

from bisect import bisect_right
 
A,B,Q = map(int,input().split())
s = [int(input()) for i in range(A)]
t = [int(input()) for i in range(B)]
ans =[]
for i in range(0,Q,1):
    tmpans = INF

    q = int(input())
    sr = bisect_right(s,q)
    sl = sr-1
    sr = min(sr,A-1)
    sl = max(0,sl)
    for j in (sr,sl):
        tr = bisect_right(t,s[j])
        tl = tr-1
        tr = min(tr,B-1)
        tl = max(0,tl)
        ansR=abs(s[j]-q)+abs(s[j]-t[tr])
        ansL=abs(s[j]-q)+abs(s[j]-t[tl])
        tmpans = min(tmpans,ansR,ansL)

    
    tr = bisect_right(t,q)
    tl = tr-1
    tr = min(tr,B-1)
    tl = max(0,tl)
    for j in (tr,tl):
        sr = bisect_right(s,t[j])
        sl = sr-1
        sr = min(sr,A-1)
        sl = max(0,sl)
        ansR=abs(t[j]-q)+abs(t[j]-s[sr])
        ansL=abs(t[j]-q)+abs(t[j]-s[sl])
        tmpans = min(tmpans,ansR,ansL)
    
    ans.append(tmpans)

for i in range(0,Q,1):
    print(ans[i])