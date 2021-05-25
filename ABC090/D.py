#bを固定すればaの個数をo(1)で計算できそうぷりね

N,K = map(int,input().split())

ans = 0

for b in range(1,N+1,1):
    ans += max(0,(b-K))*(N//b) + max(0,(N%b-K+1))
    if K ==0:#a=0がはいってしまうので引く
        ans-=1

print(ans)