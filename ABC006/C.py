N,M = map(int,input().split())

for O in range(N+1):
    if 0<=M+O-3*N and 0<=4*N-M-2*O:
        print(O,4*N-M-2*O,M+O-3*N)
        exit()

print(-1,-1,-1)