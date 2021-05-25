def atoNum(s):
    return ord(s)-97
where = [[]for i in range(0,26,1)]
from bisect import bisect_right

s = list(input())
t = list(input())

for i in range(0,len(s),1):
    where[atoNum(s[i])].append(i)
ans = 0
cersol = -1

for i in range(0,len(t),1):
    if len(where[atoNum(t[i])])==0:
        print(-1)
        exit()
    tmpCersol = bisect_right(where[atoNum(t[i])],cersol)
    if tmpCersol < len(where[atoNum(t[i])]):
        cersol = where[atoNum(t[i])][tmpCersol]
    else:
        ans += len(s)
        cersol = where[atoNum(t[i])][0]
ans += cersol
print(ans+1)