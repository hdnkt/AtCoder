S = input()
T = input()
n=len(S)
m=len(T)

mem=[[0]*(n+1) for i in range(0,m+1,1)]#それぞれs,tの左からi,j文字選んだ時のLSC

for i in range(0,n,1):
    for j in range(0,m,1):
        mem[j+1][i+1]=max([mem[j][i+1],mem[j+1][i]])
        if S[i]==T[j]:
            mem[j+1][i+1]=mem[j+1][i+1]+1

print(mem[m][n])