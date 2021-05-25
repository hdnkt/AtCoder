N = int(input())
s = [input() for i in range(N)]
M = int(input())
t = [input() for i in range(M)]

dic={}
for i in range(N):
    if s[i] in dic:
        dic[s[i]]+=1
    else:
        dic[s[i]]=1

for i in range(M):
    if t[i] in dic:
        dic[t[i]]-=1
    else:
        dic[t[i]]=-1

print(max(0,max(dic.values())))