S = list(input())
dic = [["R","U","D"],["L","U","D"]]
for i in range(0,len(S),1):
    if not(S[i] in dic[i%2]):
        print("No")
        exit()
print("Yes")