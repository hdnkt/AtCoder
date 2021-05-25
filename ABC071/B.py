import collections

S = list(input())

c = collections.Counter(S)

ans = " "
for i in range(97,123):
    s = chr(i)

    if s in c:
        continue
    else:
        ans = s
        break

print("None" if ans ==" " else ans)


