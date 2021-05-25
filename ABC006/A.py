N = int(input())
ans = False
if N%3 == 0:
    ans = True
c = list(str(N))
if "3" in c:
    ans =True
print("YES" if ans else "NO")