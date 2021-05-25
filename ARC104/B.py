N,S = input().split()
N = int(N)
S = list(S)

ans = 0
counter = {}
for i in range(N):
    counter["A"]=0
    counter["T"]=0
    counter["G"]=0
    counter["C"]=0
    for j in range(i,N):
        counter[S[j]]+=1
        if counter["A"]==counter["T"] and counter["G"]==counter["C"]:
            ans += 1


print(ans)
