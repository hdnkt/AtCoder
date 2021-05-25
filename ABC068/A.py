N = list(input())
if len(N)==1:
    N = ["0","0"]+N
if len(N)==2:
    N = ["0"]+N
print("ABC"+"".join(N))