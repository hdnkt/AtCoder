#事前に階乗を計算しておく maximにnの最大値をいれる
maxim = 10**6+1

MOD = 10**9+7
kaijou = [1]*(maxim)
inverse = [1]*(maxim)
inverse_kaijou = [1]*(maxim)
for i in range(2,maxim):
    kaijou[i]=(kaijou[i-1]*i)%MOD
    inverse[i] = MOD - ((MOD // i) * inverse[MOD % i] % MOD)
    inverse_kaijou[i]=(inverse_kaijou[i-1]*inverse[i])%MOD

#nCr
def nCr(n,r):
    if n < r:
        return 0
    return ((kaijou[n]*inverse_kaijou[r])%MOD*inverse_kaijou[n-r])%MOD

#nHr
def nHr(n,r):
    if r == 0:
        if n == 0:
            return 1
        return 0
    return ((kaijou[n+r-1]*inverse_kaijou[n])%MOD*inverse_kaijou[r-1])%MOD

print(nHr(10,10))
print(nHr(20,10))

print(nCr(16,8))