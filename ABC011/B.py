S = list(input())


if ord(S[0]) > 96:
    S[0]=chr(ord(S[0])-32) 

for i in range(1,len(S)):
    if ord(S[i])<96:
        S[i]=chr(ord(S[i])+32)

print("".join(S))