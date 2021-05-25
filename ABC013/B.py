a=int(input())
b=int(input())

ans = min(abs(a-b),abs(10+a-b),abs(a-10-b))
print(ans)