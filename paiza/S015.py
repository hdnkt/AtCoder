def lenabc(k):#レベルkの長さ
    return 6*pow(2,k-1)-3

def abc(k,n):#レベルkのn文字目
    if n == 1:
        return "A"
    elif n == lenabc(k)//2 + 1:
        return "B"
    elif n == lenabc(k):
        return "C"
    elif n <= lenabc(k)//2:
        return abc(k-1,n-1)
    else:
        return abc(k-1,n-lenabc(k)//2-1)

k,s,t = map(int,input().split())

ans = []
for i in range(s,t+1):
    ans.append(abc(k,i))
print("".join(ans))


