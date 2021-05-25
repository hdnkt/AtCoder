s = [[],[],[]]
s[0]=list(input())
s[1]=list(input())
s[2]=list(input())

a = [0 for i in range(len(s))]

dic={"a":0,"b":1,"c":2}

ans = {"a":"A","b":"B","c":"C"}

now = "a"
while 1:
    if a[dic[now]]==len(s[dic[now]]):
        print(ans[now])
        break
    tmp = s[dic[now]][a[dic[now]]]
    a[dic[now]]+=1
    now=tmp
