N = int(input())
S = input()

tmp = "b"
flag = False
for i in range(101):
    if tmp == S:
        ans=i
        flag=True
        break
    if i%3==0:
        tmp = "a"+tmp+"c"
    elif i%3==1:
        tmp = "c"+tmp+"a"
    else:
        tmp="b"+tmp+"b"
else:
    print(-1)
    exit()

print(ans)



