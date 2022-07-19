def sieve(n):
    is_prime = [True]*(n+1)
    is_prime[0] = False
    table = []

    for i in range(2, n+1):
        if is_prime[i-1]:
            table.append(i)
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    
    return is_prime, table

N,K=map(int,input().split())
flag,tabel=sieve(N)
print(tabel)
print(len(tabel))