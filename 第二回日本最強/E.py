def kaibun(N):
    ham = 0
    for i in range(len(N)):
        if N[i]!=N[len(N)-1-i]:
            ham+=1
    return ham

def sp(N):
    n = len(N)
    return N[0:n//2], N[n-n//2:n]

def level(N):
    ret = 0
    while len(N)>0:
        if kaibun(N)==0:
            ret+=1
            N,g = sp(N)
        else:
            break
    return ret

K = int(input())
S = input()

print(level(S))

if 2**(K-1) > len(S) or 2**K < len(S):
    print("impossible")

