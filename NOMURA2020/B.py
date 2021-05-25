T = list(input())
for i in range(0,len(T),1):
    if T[i]=="?":
        T[i]="D"
print("".join(T))