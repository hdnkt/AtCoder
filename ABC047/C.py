S = input()

count = 0
tmp=S[0]
for i in range(len(S)):
    if tmp!=S[i]:
        count+=1
        tmp=S[i]
print(count)