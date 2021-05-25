a,b,c,d=map(int,input().split())
s,t=map(int,input().split())

ans = s*a+t*b

if s+t >= d:
    ans-= c*(s+t)
print(ans)