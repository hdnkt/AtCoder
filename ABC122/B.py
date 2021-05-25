dic = ["A","T","G","C"]
S = list(input())

ans = 0
count = 0
for i in range(0,len(S),1):
    if S[i] in dic:
        count += 1
        ans = max(ans,count)
    else:
        count=0
print(ans)
