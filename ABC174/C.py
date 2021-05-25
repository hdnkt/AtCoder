K = int(input())

if K ==2 or K == 5 or K%2==0:
    print(-1)
    exit()

preamari = 7%K
ans = 1
while preamari != 0:
    preamari = (preamari*10 + 7%K)%K
    ans+=1

print(ans)
    


    