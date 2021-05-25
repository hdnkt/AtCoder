N = int(input())
d = []
for i in range(0,N,1):
    d.append(int(input()))
print(len(list(set(d))))