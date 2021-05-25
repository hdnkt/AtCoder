N = int(input())
S = list(input().split())

dic = {}
for i in range(N):
    if S[i] in dic:
        dic[S[i]]+=1
    else:
        dic[S[i]]=0

print("Four" if len(dic)==4 else "Three")