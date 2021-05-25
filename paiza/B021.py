N = int(input())
ans = []
for i in range(N):
    s = input()
    if (s[len(s)-1] in ["s","o","x"]) or (s[len(s)-2:len(s)] in ["sh","ch"]):
        s = s+"es"
    elif s[len(s)-1]=="f":
        s = s[0:len(s)-1]+"ves"
    elif s[len(s)-2:len(s)]=="fe":
        s = s[0:len(s)-2]+"ves"
    elif s[len(s)-1]=="y" and not(s[len(s)-2] in ["a","i","u","e","o"]):
        s = s[0:len(s)-1]+"ies"
    else:
        s = s+"s"

    ans.append(s)

for i in range(N):
    print(ans[i])
