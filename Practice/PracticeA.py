import re
s = input()
if re.fullmatch("(dream|dreamer|erase|eraser)+",s)==None:
    print("NO")
else:
    print("YES")