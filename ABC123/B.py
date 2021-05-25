import itertools

A = [int(input())for i in range(0,5,1)]

ans = 10**10
for Atmp in list(itertools.permutations(A)):
    time = 0
    for i in range(0,5,1):
        if time%10 != 0:
            time += (10-time%10)
        time += Atmp[i]
    ans = min(ans,time)
print(ans)



    
