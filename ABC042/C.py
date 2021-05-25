N,K = map(int,input().split())

D = list(input().split())

for i in range(1000000):
    if i < N:
        continue

    tmp = list(str(i))

    flag=True
    for j in range(len(tmp)):
        if tmp[j] in D:
            flag=False
            break
    if flag:
        print(i)
        break