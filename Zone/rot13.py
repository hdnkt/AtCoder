print(ord("{"))

dec = []

for i in range(31):
    dec.append(input())

ans = []
for i in range(31):
    tmp = []
    for j in range(len(dec[i])):
        tmp.append(chr(ord(dec[i][j])+13 if ord(dec[i][j])+13 < 123 else ord(dec[i][j])+13-26))
    ans.append("".join(tmp))

print()
for i in range(31):
    print(ans[i])
