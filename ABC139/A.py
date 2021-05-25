S = input()
T = input()
count=0
for i in range(0,3,1):
    if S[i]==T[i]:
        count+=1

print(count)