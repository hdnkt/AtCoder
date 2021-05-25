N = int(input())
T = input()

if len(T)>=3:
    flag=True
    ch = [T[0],T[1],T[2]]

    for i in range(len(T)):
        if T[i]!=T[i%3]:
            flag=False

    ch.sort()
    if not(ch[0]=="0" and ch[1]=="1" and ch[2]=="1"):
        flag=False
    
    if flag==False:
        print(0)
        exit()

if T=="00":
    print(0)
    exit()


if T=="11":
    print(10**10)
    exit()
elif T=="1":
    print(2*(10**10))
    exit()
else:
    le = len(T)
    if T[0:2]=="10":
        le+=1
    elif T[0:1]=="0":
        le+=2
    ans = 10**10 - (le//3)
    if le%3==0:
        ans+=1

print(ans)