N = int(input())

ans = 0
for i in range(21):
    if i%3 != 0:
        continue
    
    tmp = 10**i

    if N >= tmp:
        ans += (min(N,10**(i+3)-1)-tmp+1)*(i//3)

print(ans)