X = input()

X = X.replace("ch","o")

flag=True
for i in range(len(X)):
    if not(X[i] in ["o","k","u"]):
        flag=False

print("YES" if flag else "NO")