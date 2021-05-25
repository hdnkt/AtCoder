def nCk(n,k):
    res = 1
    for i in range(k,0,-1):
        res = res*(n+1-i)/i
    return int(res)

N=input()
K=int(input())

if len(N) < K:
    print("0")
if len(N) ==1:
    print(N[0])#一つもない場合と１ケタを例外処理
ans = 0
for i in range(1,len(N),1):#ex)8357 ~999
    if i < K:
        continue
    ans += pow(9,K) * nCk(i-1,K-1)

ans += (int(N[0])-1)*pow(9,K-1)*nCk(len(N)-1,K-1)#1000~7999

print(ans)
if K == 1:
    print(ans)
    exit()
next_no0 = 0
for i in range(2,K+1,1):
    for j in range(next_no0 + 1,len(N)+1,1):
        if j == len(N):
            print(ans)
            exit()
        if N[j]!="0":
            next_no0 = j
            break
    ans += (int(N[next_no0]))*pow(9,K-i)*nCk(len(N)-next_no0-1,K-i)
    print(i,next_no0)

print(ans)
