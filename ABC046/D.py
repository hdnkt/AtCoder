s = list(input())

acd = ["g"]*(len(s)//2)
if len(s)%2==1:
    acd=acd+["g"]
acd = acd+["p"]*(len(s)//2)

ans = 0
for i in range(len(s)):
    if s[i]=="g" and acd[i]=="p":
        ans+=1
    elif s[i]=="p" and acd[i]=="g":
        ans-=1

print(ans)