N,Q = map(int,input().split())
c = list(map(int,input().split()))
#ここまでにでてきた種類、とここまでにしかないものの種類

kokomade_syurui = [0]*(N)
dic = {}
for i in range(N):#ここまでに出てきた種類数
    if c[i] in dic:
        dic[c[i]]+=1
    else:
        dic[c[i]]=1
    kokomade_syurui[i]=len(dic)

dic_backup = dic

koremade_syurui = [0]*(N)
for i in range(N):#ここまでにしかない。最後のcを累積和とる
    dic[c[i]]-=1
    if dic[c[i]]==0:
        koremade_syurui[i]=1
for i in range(1,N):
    koremade_syurui[i]=koremade_syurui[i]+koremade_syurui[i-1]

dic = {}
for i in range(N):#ここまでに出てきた種類数
    if c[i] in dic:
        dic[c[i]]+=1
    else:
        dic[c[i]]=1
    kokomade_syurui[i]=len(dic)
usirokaramita_koremade = [0]*(N)
print(dic_backup)
for i in range(N-1,-1,-1):
    dic[c[i]]-=1
    if dic[c[i]]==0:
        usirokaramita_koremade[i]=1
print(usirokaramita_koremade)
for i in range(N-2,-1,-1):
    usirokaramita_koremade[i]=usirokaramita_koremade[i]+usirokaramita_koremade[i+1]
print(usirokaramita_koremade)
koremade_syurui = [0]+koremade_syurui
kokomade_syurui = [0]+kokomade_syurui
usirokaramita_koremade = [usirokaramita_koremade[0]] + usirokaramita_koremade+[0]

ans = []
for i in range(Q):
    l,r = map(int,input().split())
    ans.append(len(dic)-usirokaramita_koremade[r+2] -koremade_syurui[l-1])


print(ans)
print(usirokaramita_koremade)
print(koremade_syurui)
print(len(dic))