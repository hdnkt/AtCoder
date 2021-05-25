S = list(input())
ans = [0]*len(S)

i = 0
while i < len(S):
    Rcount=0
    while S[i]=="R":
        Rcount += 1
        i += 1
    ans[i]+=Rcount//2
    ans[i-1]+=Rcount//2+Rcount%2

    terminal = i
    Lcount=0
    while i < len(S) and S[i]=="L":
        Lcount+=1
        i += 1
    ans[terminal]+=Lcount//2+Lcount%2
    ans[terminal-1]+=Lcount//2

print(" ".join(map(str,ans)))

