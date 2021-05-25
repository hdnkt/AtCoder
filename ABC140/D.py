N,K = map(int,input().split())
S = list(input())
i=1
count =0
owari = False
while i < N:
    if S[i]!=S[0]:
        for j in range(i,N,1):
            if S[j]!=S[0]:
                S[j]=S[0]
            else:
                i = j
                break
            if j==N-1:
                i=N
        count+=1
        if count >= K:
            owari = True
    i+=1
    if owari:
        break
score=0
for i in range(0,N,1):
    if S[i]=="R":
        if i < N-1 and S[i+1]==S[i]:
            score+=1
    else:
        if i > 0 and S[i-1]==S[i]:
            score+=1
print(score)