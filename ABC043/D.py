from collections import deque

s = list(input())

if len(s)==2:
    if s[0]==s[1]:
        print(1,2)
    else:
        print(-1,-1)
    exit()

q = deque([])
q.append(s[0])
q.append(s[1])

for i in range(2,len(s)):
    if s[i] in q:
        print(i-1,i+1)
        exit()
    else:
        q.popleft()
        q.append(s[i])

print(-1,-1)
