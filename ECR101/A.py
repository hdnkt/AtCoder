T = int(input())

ans = []
for t in range(T):
    flag = True
    s = input()
    if len(s)%2==1:
        flag=False
    else:
        A = 0
        B = 0
        C = 0
        for i in range(len(s)):
            if s[i]=="(":
                A+=1
            elif s[i]==")":
                B+=1
            else:
                C+=1
            if B > A+C:
                flag=False
        if A > len(s)//2 or B > len(s)//2:
            flag=False
        A = 0
        B = 0
        C = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="(":
                A+=1
            elif s[i]==")":
                B+=1
            else:
                C+=1
            if A > B+C:
                flag=False
        if A > len(s)//2 or B > len(s)//2:
            flag=False
    
    ans.append("YES" if flag else "NO")

for i in range(T):
    print(ans[i])
