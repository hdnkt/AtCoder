MOD = 10**9 + 7

N,P = map(int,input().split())

ans = (P-1)*pow(P-2,N-1,MOD)

print(ans%MOD)