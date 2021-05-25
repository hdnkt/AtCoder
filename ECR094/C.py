T = int(input())

ans = []
for i in range(T):
    s = list(input())
    x = int(input())
    w = ["1"]*len(s)
    #0の条件で作って1の条件でチェック
    for i in range(len(s)):
        if s[i]=="0":
            if i-x>=0:
                w[i-x]="0"
            if i+x <len(s):
                w[i+x]="0"

    is_Ok = True
    for i in range(len(s)):
        if s[i]=="1":
            if i-x>=0:
                if w[i-x]=="1":
                    continue
            if i+x <len(s):
                if w[i+x]=="1":
                    continue
            is_Ok=False
    
    if is_Ok:
        ans.append(w)
    else:
        ans.append(["-1"])

for i in range(T):
    print("".join(ans[i]))

