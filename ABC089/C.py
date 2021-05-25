import itertools

N = int(input())

dic = {"M":{},"A":{},"R":{},"C":{},"H":{}}

for i in range(0,N,1):
    s = input()
    if s[0] in dic:
        dic[s[0]][s]=0

ans = 0
for i in itertools.combinations(["M","A","R","C","H"],3):
    ans+= len(dic[i[0]])*len(dic[i[1]])*len(dic[i[2]])

print(ans)