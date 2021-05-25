dic = {"+":1,"-":-1}
ans =0
S = list(input())
for i in range(4):
    ans+=dic[S[i]]
print(ans)