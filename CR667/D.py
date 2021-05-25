T = int(input())

ret = []
for t in range(T):
    n,s = input().split()
    s = int(s)
    raw = int(n)
    n = list(n)
    n = list(map(int,n))

    score = sum(n)

    ans = 0#手数
    keta = 0
    while score > s:#len(n)-1-ketaであくせすかなあ
        if n[len(n)-1-keta] == 0:
            keta+=1
            continue
        if n[len(n)-1-keta] == 10:
            n[max(0,len(n)-1-keta-1)]+=1
            keta+=1
            score += -9
            continue
        score += 1 - n[len(n)-1-keta]
        ans += (10**keta)*(10-n[len(n)-1-keta])
        n[max(0,len(n)-1-keta-1)]+=1
        keta+=1
    
    ret.append(ans)

for i in range(T):
    print(ret[i])
