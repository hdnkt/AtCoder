H1,M1,H2,M2,K = map(int,input().split())

H = H2 - H1
M = M2 - M1

time = H*60 + M

print(time-K)
